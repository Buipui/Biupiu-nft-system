use bevy::prelude::*;
use std::collections::BTreeMap;

#[derive(Resource, Debug, Default, Clone, Copy)]
pub struct BiupiuBevyRuntime { pub tick: u64, pub simulation_enabled: bool }

#[derive(Message, Debug, Clone, PartialEq, Eq)]
pub struct BiupiuSimulationEvent { pub domain: String, pub action: String }

#[derive(Debug, Clone, PartialEq)]
pub struct SimulationEntity { pub id: String, pub kind: String, pub state: BTreeMap<String, f64> }

#[derive(Resource, Debug, Default)]
pub struct BiupiuSimulationKernel {
    pub simulation_id: String,
    pub tick: u64,
    pub running: bool,
    pub entities: BTreeMap<String, SimulationEntity>,
    pub measurements: Vec<SimulationMeasurement>,
}

#[derive(Debug, Clone, PartialEq)]
pub struct SimulationMeasurement {
    pub simulation_id: String,
    pub tick: u64,
    pub entity_id: String,
    pub metric: String,
    pub value: f64,
}

impl BiupiuSimulationKernel {
    pub fn new(simulation_id: impl Into<String>) -> Self { Self { simulation_id: simulation_id.into(), ..Default::default() } }
    pub fn register_entity(&mut self, entity: SimulationEntity) -> Result<(), String> {
        if entity.id.trim().is_empty() { return Err("entity id must not be empty".into()); }
        if self.entities.contains_key(&entity.id) { return Err(format!("entity already registered: {}", entity.id)); }
        self.entities.insert(entity.id.clone(), entity); Ok(())
    }
    pub fn start(&mut self) { self.running = true; }
    pub fn pause(&mut self) { self.running = false; }
    pub fn step(&mut self) { if self.running { self.tick = self.tick.saturating_add(1); } }
    pub fn record_measurement(&mut self, entity_id: &str, metric: impl Into<String>, value: f64) -> Result<(), String> {
        if !self.entities.contains_key(entity_id) { return Err(format!("unknown entity: {entity_id}")); }
        self.measurements.push(SimulationMeasurement { simulation_id: self.simulation_id.clone(), tick: self.tick, entity_id: entity_id.into(), metric: metric.into(), value }); Ok(())
    }
}

#[derive(Default)]
pub struct BiupiuBevyPlugin;

impl Plugin for BiupiuBevyPlugin {
    fn build(&self, app: &mut App) {
        app.init_resource::<BiupiuBevyRuntime>().init_resource::<BiupiuSimulationKernel>()
            .add_message::<BiupiuSimulationEvent>().add_systems(Update, advance_runtime_tick);
    }
}
fn advance_runtime_tick(mut runtime: ResMut<BiupiuBevyRuntime>) { runtime.tick = runtime.tick.saturating_add(1); }

#[cfg(test)]
mod tests {
    use super::*;
    #[test] fn runtime_state_starts_disabled() { let s=BiupiuBevyRuntime::default(); assert_eq!(s.tick,0); assert!(!s.simulation_enabled); }
    #[test] fn plugin_registers_runtime_and_kernel() {
        let mut app=App::new(); app.add_plugins(BiupiuBevyPlugin::default()); app.update();
        assert_eq!(app.world().resource::<BiupiuBevyRuntime>().tick,1);
        assert_eq!(app.world().resource::<BiupiuSimulationKernel>().tick,0);
    }
    #[test] fn kernel_rejects_duplicate_and_unknown_entities() {
        let mut k=BiupiuSimulationKernel::new("SIM-001");
        let e=SimulationEntity{id:"E-001".into(),kind:"test".into(),state:BTreeMap::new()};
        assert!(k.register_entity(e.clone()).is_ok()); assert!(k.register_entity(e).is_err());
        assert!(k.record_measurement("UNKNOWN","value",1.0).is_err());
    }
    #[test] fn kernel_advances_and_records() {
        let mut k=BiupiuSimulationKernel::new("SIM-001");
        k.register_entity(SimulationEntity{id:"E-001".into(),kind:"test".into(),state:BTreeMap::new()}).unwrap();
        k.step(); assert_eq!(k.tick,0); k.start(); k.step(); assert_eq!(k.tick,1);
        k.record_measurement("E-001","velocity",12.5).unwrap(); assert_eq!(k.measurements[0].tick,1);
    }
    #[test] fn replay_fixture_is_deterministic() {
        fn run()->Vec<(u64,f64)> {
            let mut k=BiupiuSimulationKernel::new("REPLAY-001");
            k.register_entity(SimulationEntity{id:"E-001".into(),kind:"test".into(),state:BTreeMap::new()}).unwrap(); k.start();
            for v in [1.0,2.0,3.0] { k.step(); k.record_measurement("E-001","value",v).unwrap(); }
            k.measurements.into_iter().map(|m|(m.tick,m.value)).collect()
        }
        assert_eq!(run(),run());
    }
}
