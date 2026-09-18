# UE 5.6.1 / UE 5.8.1 MCP Verification Matrix

Status is intentionally conservative: the upstream PR documents compile/link proof for UE 5.8.1, while the full two-engine runtime matrix remains to be demonstrated.

| Gate | UE 5.6.1 | UE 5.8.1 |
|---|---|---|
| UBT compile | PENDING | DOCUMENTED PASS upstream |
| Link | PENDING | DOCUMENTED PASS upstream |
| Editor load | PENDING | PENDING |
| MCP bind/start | PENDING | PENDING |
| TypeScript suite | PENDING | PENDING |
| Tool registration | PENDING | PENDING |
| Blueprint smoke | PENDING | PENDING |
| DataAsset/UserDefinedStruct | PENDING | PENDING |
| Material validation | PENDING | PENDING |
| Animation mutation | PENDING | PENDING |
| PIE/runtime smoke | PENDING | PENDING |
| Vision/capture smoke | PENDING | PENDING |

## Promotion rule
verified may only be assigned after the relevant engine passes compile, link, editor load, MCP startup and representative runtime smoke tests.

This matrix is a Biupiu integration record; it does not claim tests were executed locally by this repository.
