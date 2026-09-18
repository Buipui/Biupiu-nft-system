# Biupiu Department Module Contract v1

Gate 16 binds each entitled department route to a concrete module identity, launch URI, package identity, and native screen ID.

## Module map

| ID | Package | URI | Screen |
|---|---|---|---|
| SMART_FARMING | @biupiu/smart-farming | biupiu://department/smart-farming | FARMING_WORLD |
| SMART_METAL_WORKSHOP | @biupiu/smart-metallurgy | biupiu://department/smart-metal-workshop | METAL_MAKING_WORLD |
| RND_OS | @biupiu/rnd-os | biupiu://department/rnd-os | RND_OS_HOME |

The contract is platform-neutral. Android and Windows maintain native registries that consume the same mapping. Windows OS-level protocol registration remains an installer/package concern and is not claimed by this gate.
