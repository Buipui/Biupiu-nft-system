use bevy::prelude::*;

#[derive(Resource, Debug, Default, Clone, Copy)]
pub struct BiupiuBevyRuntime {
    pub tick: u64,
    pub simulation_enabled: bool,
}

#[derive(Message, Debug, Clone)]
pub struct BiupiuSimulationEvent {
    pub domain: String,
    pub action: String,
}

#[derive(Default)]
pub struct BiupiuBevyPlugin;

impl Plugin for BiupiuBevyPlugin {
    fn build(&self, app: &mut App) {
        app.init_resource::<BiupiuBevyRuntime>()
            .add_message::<BiupiuSimulationEvent>()
            .add_systems(Update, advance_runtime_tick);
    }
}

fn advance_runtime_tick(mut runtime: ResMut<BiupiuBevyRuntime>) {
    runtime.tick = runtime.tick.saturating_add(1);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn runtime_state_starts_disabled() {
        let state = BiupiuBevyRuntime::default();
        assert_eq!(state.tick, 0);
        assert!(!state.simulation_enabled);
    }

    #[test]
    fn plugin_registers_runtime_resource() {
        let mut app = App::new();
        app.add_plugins(BiupiuBevyPlugin::default());
        app.update();

        let runtime = app.world().resource::<BiupiuBevyRuntime>();
        assert_eq!(runtime.tick, 1);
    }
}
