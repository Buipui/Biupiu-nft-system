# SF-13 — Biupiu World Runtime Architecture

## Goal
Enable Biupiu OS to launch and manage Biupiu World functions from one runtime while keeping the world content modular.

## Runtime modules
- World Launcher
- Campus/Environment Loader
- Facility Interaction Engine
- Avatar Manager
- Home/Property Manager
- Marketplace UI
- Digital Gallery
- Academy/Learning Manager
- Digital Laboratory Bridge
- Research Library Bridge
- Intelligence Hub Context Bridge
- Account/Entitlement Manager

## World session
A world session carries user_id, environment_id, facility_id, avatar_id, property_id, lesson_id and experiment_id. Only fields authorised for the user's account are exposed to each module.

## Asset policy
The runtime supports original Biupiu assets, properly licensed third-party assets and public-domain/open-licence assets. Game-extracted Assassin's Creed assets, character models, textures or environments are not added to the Biupiu commercial repository unless Ubisoft and any applicable creators grant explicit rights.

## Import pipeline
Source asset -> licence/rights check -> provenance record -> security scan -> format conversion -> optimisation -> visual/cultural review -> approved catalogue -> runtime package.
