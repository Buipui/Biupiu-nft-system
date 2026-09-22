#[repr(C)]
#[derive(Copy, Clone, Eq, PartialEq, Debug)]
pub enum ComputeClass { Cpu=0, Vector=1, Gpu=2, Npu=3 }

#[repr(C)]
#[derive(Copy, Clone)]
pub struct ComputeUnit {
    pub unit_id:u32,
    pub compute_class:ComputeClass,
    pub capacity:u32,
    pub available:u32
}

#[repr(C)]
pub struct Workload {
    pub workload_id:u32,
    pub cost:u32,
    pub preferred_class:ComputeClass,
    pub minimum_class:ComputeClass
}

/// Mini-OS contract:
/// - minimum_class is an exact hard requirement; a different accelerator
///   never satisfies it merely because its enum value is numerically higher.
/// - preferred_class is a preference within that required class.
/// - because this ABI carries one minimum class, a different preferred class
///   cannot override the hard minimum; capacity is used as the fallback signal.
pub fn select_compute(units:&[ComputeUnit], workload:&Workload)->Option<u32>{
    let mut best:Option<ComputeUnit>=None;

    for unit in units.iter().copied(){
        if unit.available==0 || unit.capacity==0 || unit.compute_class != workload.minimum_class {
            continue;
        }

        if unit.compute_class==workload.preferred_class {
            return Some(unit.unit_id);
        }

        if best.map_or(true,|b|unit.capacity>b.capacity){
            best=Some(unit);
        }
    }

    best.map(|u|u.unit_id)
}

#[cfg(test)]
mod tests{
    use super::*;

    #[test]
    fn gpu_preferred_and_required(){
        let units=[
            ComputeUnit{unit_id:1,compute_class:ComputeClass::Cpu,capacity:2,available:1},
            ComputeUnit{unit_id:2,compute_class:ComputeClass::Gpu,capacity:8,available:1},
        ];
        let gpu=Workload{
            workload_id:1,
            cost:10,
            preferred_class:ComputeClass::Gpu,
            minimum_class:ComputeClass::Gpu
        };
        assert_eq!(select_compute(&units,&gpu),Some(2));
    }

    #[test]
    fn preferred_class_cannot_override_hard_minimum(){
        let units=[
            ComputeUnit{unit_id:1,compute_class:ComputeClass::Cpu,capacity:4,available:1},
            ComputeUnit{unit_id:2,compute_class:ComputeClass::Gpu,capacity:8,available:1},
        ];
        let workload=Workload{
            workload_id:2,
            cost:10,
            preferred_class:ComputeClass::Gpu,
            minimum_class:ComputeClass::Cpu
        };
        assert_eq!(select_compute(&units,&workload),Some(1));
    }

    #[test]
    fn missing_required_npu_fails_closed(){
        let units=[
            ComputeUnit{unit_id:1,compute_class:ComputeClass::Cpu,capacity:2,available:1},
            ComputeUnit{unit_id:2,compute_class:ComputeClass::Gpu,capacity:8,available:1},
        ];
        let npu=Workload{
            workload_id:3,
            cost:1,
            preferred_class:ComputeClass::Npu,
            minimum_class:ComputeClass::Npu
        };
        assert_eq!(select_compute(&units,&npu),None);
    }

    #[test]
    fn capacity_is_fallback_within_required_class(){
        let units=[
            ComputeUnit{unit_id:1,compute_class:ComputeClass::Cpu,capacity:2,available:1},
            ComputeUnit{unit_id:2,compute_class:ComputeClass::Cpu,capacity:8,available:1},
        ];
        let workload=Workload{
            workload_id:4,
            cost:1,
            preferred_class:ComputeClass::Gpu,
            minimum_class:ComputeClass::Cpu
        };
        assert_eq!(select_compute(&units,&workload),Some(2));
    }
}
