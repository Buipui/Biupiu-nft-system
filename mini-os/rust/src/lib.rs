pub mod federation;

#[repr(C)]
#[derive(Copy, Clone, Eq, PartialEq, Debug)]
pub enum MiniStatus {
    Ok = 0,
    InvalidArgument = 1,
    NotReady = 2,
    Conflict = 3,
    PermissionDenied = 4,
}

#[repr(C)]
pub struct MiniCapability {
    pub abi_version: u32,
    pub struct_size: u32,
    pub capability_bits: u64,
}

#[no_mangle]
pub extern "C" fn biupiu_mini_get_capability(out: *mut MiniCapability) -> MiniStatus {
    if out.is_null() {
        return MiniStatus::InvalidArgument;
    }

    // SAFETY: out is checked for null above. The C ABI contract requires
    // callers to provide a valid, writable MiniCapability pointer for the
    // duration of this call, and the function writes only that struct.
    unsafe {
        (*out).abi_version = 1;
        (*out).struct_size = core::mem::size_of::<MiniCapability>() as u32;
        (*out).capability_bits = 0;
    }
    MiniStatus::Ok
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn rejects_null_output() {
        assert_eq!(
            biupiu_mini_get_capability(core::ptr::null_mut()),
            MiniStatus::InvalidArgument
        );
    }

    #[test]
    fn exposes_versioned_capability() {
        let mut cap = MiniCapability {
            abi_version: 0,
            struct_size: 0,
            capability_bits: 99,
        };
        assert_eq!(
            biupiu_mini_get_capability(&mut cap),
            MiniStatus::Ok
        );
        assert_eq!(cap.abi_version, 1);
        assert_eq!(cap.struct_size as usize, core::mem::size_of::<MiniCapability>());
        assert_eq!(cap.capability_bits, 0);
    }
}
