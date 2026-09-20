#![deny(unsafe_op_in_unsafe_fn)]

use core::ffi::c_void;

#[repr(C)]
pub struct BiupiuCapability {
    pub abi_version: u32,
    pub struct_size: u32,
    pub capability_bits: u64,
}

#[repr(C)]
#[derive(Copy, Clone, Eq, PartialEq, Debug)]
pub enum BiupiuStatus {
    Ok = 0,
    InvalidArgument = 1,
    NotReady = 2,
    Conflict = 3,
    PermissionDenied = 4,
}

#[repr(C)]
pub struct BiupiuBytes {
    pub data: *const c_void,
    pub size: u64,
}

#[no_mangle]
pub extern "C" fn biupiu_core_get_capability(out: *mut BiupiuCapability) -> BiupiuStatus {
    if out.is_null() {
        return BiupiuStatus::InvalidArgument;
    }
    // SAFETY: the caller contract requires a valid writable pointer when non-null.
    unsafe {
        (*out).abi_version = 1;
        (*out).struct_size = core::mem::size_of::<BiupiuCapability>() as u32;
        (*out).capability_bits = 0;
    }
    BiupiuStatus::Ok
}

#[no_mangle]
pub extern "C" fn biupiu_core_validate_buffer(input: BiupiuBytes) -> BiupiuStatus {
    if input.size > 0 && input.data.is_null() {
        return BiupiuStatus::InvalidArgument;
    }
    BiupiuStatus::Ok
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn null_capability_pointer_is_rejected() {
        assert_eq!(
            biupiu_core_get_capability(core::ptr::null_mut()),
            BiupiuStatus::InvalidArgument
        );
    }

    #[test]
    fn capability_contract_is_populated() {
        let mut cap = BiupiuCapability {
            abi_version: 0,
            struct_size: 0,
            capability_bits: u64::MAX,
        };
        assert_eq!(
            biupiu_core_get_capability(&mut cap),
            BiupiuStatus::Ok
        );
        assert_eq!(cap.abi_version, 1);
        assert_eq!(
            cap.struct_size as usize,
            core::mem::size_of::<BiupiuCapability>()
        );
        assert_eq!(cap.capability_bits, 0);
    }

    #[test]
    fn invalid_nonempty_null_buffer_is_rejected() {
        let input = BiupiuBytes {
            data: core::ptr::null(),
            size: 1,
        };
        assert_eq!(
            biupiu_core_validate_buffer(input),
            BiupiuStatus::InvalidArgument
        );
    }

    #[test]
    fn empty_null_buffer_is_valid() {
        let input = BiupiuBytes {
            data: core::ptr::null(),
            size: 0,
        };
        assert_eq!(biupiu_core_validate_buffer(input), BiupiuStatus::Ok);
    }
}
