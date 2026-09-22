# Stage 9 — Windows Execution + End-to-End Pipeline Foundation
Implemented:
- Render-job validation.
- Execution-state lifecycle.
- Windows runner preparation boundary.
- Automated validation test covering valid/invalid jobs.
- Clear separation between repository code and the locally installed licensed KeyShot runtime.

## End-to-end target
Biupiu asset -> render-job contract -> validation -> Windows KeyShot runner -> rendered output -> Output Registry -> Showcase/Digital Twin/Showreel.

## Current limitation
The repository can prepare and validate the execution command, but actual rendering requires a Windows machine with a licensed KeyShot installation and its approved command-line/API invocation configured.

## Acceptance gate
No render command is executed until validation succeeds and a real licensed KeyShot executable is supplied at deployment time.
