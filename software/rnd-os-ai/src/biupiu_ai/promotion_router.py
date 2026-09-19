"""Fail-closed promotion routing for research learned by Biupiu Intelligence.

This module only creates a promotion proposal. Main OS remains authoritative.
"""
from dataclasses import dataclass
from enum import Enum

class AssetClass(str, Enum):
    REFERENCE="reference"
    PATTERN="pattern"
    ADAPTER="adapter"
    ASSET="asset"
    DEPENDENCY="dependency"
    PROHIBITED="prohibited"

@dataclass(frozen=True)
class PromotionProposal:
    record_id: str
    asset_class: AssetClass
    departments: tuple[str, ...]
    main_os_approval_required: bool = True
    digital_twin_eligible: bool = False

def propose_promotion(*, record_id: str, asset_class: AssetClass,
                      departments: tuple[str, ...] = (),
                      licence_verified: bool = False,
                      security_checked: bool = False,
                      compatibility_checked: bool = False,
                      deterministic_tests_passed: bool = False,
                      provenance_recorded: bool = False,
                      human_approved: bool = False) -> PromotionProposal:
    if not record_id:
        raise ValueError("record_id is required")
    if asset_class is AssetClass.PROHIBITED:
        return PromotionProposal(record_id, asset_class, tuple(dict.fromkeys(departments)))
    eligible = all((licence_verified, security_checked, compatibility_checked,
                    deterministic_tests_passed, provenance_recorded, human_approved))
    return PromotionProposal(
        record_id,
        asset_class,
        tuple(dict.fromkeys(departments)),
        main_os_approval_required=True,
        digital_twin_eligible=eligible and asset_class in {
            AssetClass.ADAPTER, AssetClass.ASSET, AssetClass.DEPENDENCY
        },
    )
