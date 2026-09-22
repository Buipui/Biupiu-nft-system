import json
from pathlib import Path


class FailureGovernance:
    """Persistence, clustering and approval workflow for failure evidence."""

    def __init__(self, path=None):
        self.path = Path(path) if path else None
        self.proposals = []

    def persist(self, records):
        if not self.path:
            return False
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(records, indent=2, sort_keys=True), encoding="utf-8")
        return True

    def clusters(self, records):
        grouped = {}
        for record in records:
            grouped.setdefault(record["signature"], []).append(record)
        return [
            {"signature": signature, "count": len(items), "modules": sorted({x["module"] for x in items}),
             "categories": sorted({x["category"] for x in items}), "issues": sorted({issue for x in items for issue in x["issues"]})}
            for signature, items in sorted(grouped.items())
        ]

    def propose_remediation(self, cluster):
        return {
            "proposal_id": f"remediate-{cluster['signature']}",
            "signature": cluster["signature"],
            "status": "pending_human_approval",
            "action": "investigate_and_define_remediation",
            "reason": "recurring failure signature",
        }

    def approve(self, proposal_id):
        for proposal in self.proposals:
            if proposal["proposal_id"] == proposal_id:
                proposal["status"] = "approved"
                return proposal
        raise KeyError(proposal_id)
