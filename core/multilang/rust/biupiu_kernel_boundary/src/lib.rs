#![deny(unsafe_op_in_unsafe_fn)]

use core::ffi::c_void;

#[repr(C)]
pub struct BiupiuCapability {
    pub abi_version: u32,
    pub struct_size: u32,
    pub capability_bits: u64,
}

#[repr(C)]
#[derive(Copy, Clone, Eq, PartialEq)]
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
    // SAFETY: caller provides a valid writable pointer when non-null.
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
