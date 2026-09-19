# Failure Learning and Recovery v1

Failures become structured records rather than silent errors. The system classifies them, proposes bounded remediation and records outcomes for later analysis.

Only low-risk bounded retries may run automatically. Provider changes, asset replacement, configuration changes and unknown-failure remediation require authorization or human approval.

The learning layer is recommendation-first: it may improve recovery rules from audited evidence, but it cannot rewrite production code or security policy autonomously.