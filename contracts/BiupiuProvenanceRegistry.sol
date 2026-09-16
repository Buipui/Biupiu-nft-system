// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";

/// @title Biupiu Dual-Asset Bonding Registry
/// @notice Maintains cryptographic bonds between artwork and certificate NFTs.
/// @dev Tracks proof hashes and bond status for authenticity verification.
contract BiupiuProvenanceRegistry is Ownable {
    struct DualAssetBond {
        address artworkContract;
        uint256 artworkTokenId;
        address certificateContract;
        uint256 certificateTokenId;
        bytes32 proofHash;
        bytes32 manifestHash;
        uint64 bondedAt;
        bool active;
    }

    struct ProvenanceRecord {
        bytes32 researchId;
        bytes32 algorithmId;
        bytes32 algorithmVersion;
        bytes32 metadataHash;
        uint64 recordedAt;
    }

    mapping(bytes32 => DualAssetBond) public bonds; // bondId -> bond details
    mapping(bytes32 => ProvenanceRecord) public provenance; // provenanceId -> record
    mapping(bytes32 => bool) public bondExists;
    mapping(bytes32 => bool) public provenanceExists;

    error BondAlreadyExists();
    error BondNotFound();
    error ProvenanceAlreadyRecorded();
    error ProvenanceNotFound();
    error ZeroAddress();
    error InvalidHash();

    event BondRegistered(
        bytes32 indexed bondId,
        address indexed artworkContract,
        uint256 indexed artworkTokenId,
        address certificateContract,
        uint256 certificateTokenId,
        bytes32 proofHash
    );
    event ProvenanceRecorded(
        bytes32 indexed provenanceId,
        bytes32 indexed researchId,
        bytes32 indexed algorithmId,
        bytes32 metadataHash
    );
    event BondSevered(bytes32 indexed bondId);

    constructor() Ownable(msg.sender) {}

    /// @notice Register a dual-asset bond between artwork and certificate
    function registerBond(
        bytes32 bondId,
        address artworkContract,
        uint256 artworkTokenId,
        address certificateContract,
        uint256 certificateTokenId,
        bytes32 proofHash,
        bytes32 manifestHash
    ) external onlyOwner {
        if (bondExists[bondId]) revert BondAlreadyExists();
        if (artworkContract == address(0) || certificateContract == address(0))
            revert ZeroAddress();
        if (proofHash == bytes32(0) || manifestHash == bytes32(0))
            revert InvalidHash();

        bonds[bondId] = DualAssetBond({
            artworkContract: artworkContract,
            artworkTokenId: artworkTokenId,
            certificateContract: certificateContract,
            certificateTokenId: certificateTokenId,
            proofHash: proofHash,
            manifestHash: manifestHash,
            bondedAt: uint64(block.timestamp),
            active: true
        });

        bondExists[bondId] = true;

        emit BondRegistered(
            bondId,
            artworkContract,
            artworkTokenId,
            certificateContract,
            certificateTokenId,
            proofHash
        );
    }

    /// @notice Record provenance metadata on-chain as hash commitment
    function recordProvenance(
        bytes32 provenanceId,
        bytes32 researchId,
        bytes32 algorithmId,
        bytes32 algorithmVersion,
        bytes32 metadataHash
    ) external onlyOwner {
        if (provenanceExists[provenanceId]) revert ProvenanceAlreadyRecorded();
        if (
            researchId == bytes32(0)
            || algorithmId == bytes32(0)
            || metadataHash == bytes32(0)
        ) revert InvalidHash();

        provenance[provenanceId] = ProvenanceRecord({
            researchId: researchId,
            algorithmId: algorithmId,
            algorithmVersion: algorithmVersion,
            metadataHash: metadataHash,
            recordedAt: uint64(block.timestamp)
        });

        provenanceExists[provenanceId] = true;

        emit ProvenanceRecorded(
            provenanceId,
            researchId,
            algorithmId,
            metadataHash
        );
    }

    /// @notice Sever a dual-asset bond (e.g., after certificate burn)
    function severBond(bytes32 bondId) external onlyOwner {
        if (!bondExists[bondId]) revert BondNotFound();
        bonds[bondId].active = false;
        emit BondSevered(bondId);
    }

    /// @notice Get bond details
    function getBond(bytes32 bondId)
        external
        view
        returns (DualAssetBond memory)
    {
        if (!bondExists[bondId]) revert BondNotFound();
        return bonds[bondId];
    }

    /// @notice Get provenance record
    function getProvenance(bytes32 provenanceId)
        external
        view
        returns (ProvenanceRecord memory)
    {
        if (!provenanceExists[provenanceId]) revert ProvenanceNotFound();
        return provenance[provenanceId];
    }

    /// @notice Verify a bond by comparing hashes
    function verifyBond(bytes32 bondId, bytes32 expectedProofHash)
        external
        view
        returns (bool)
    {
        if (!bondExists[bondId]) return false;
        return bonds[bondId].proofHash == expectedProofHash
            && bonds[bondId].active;
    }
}
