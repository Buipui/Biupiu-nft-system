// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";

/// @title Biupiu Learning Registry
/// @notice Prototype registry for anchoring approved learning/checkpoint commitments.
/// @dev Stores hashes and identifiers only; raw datasets, prompts, model outputs and private IP stay off-chain.
contract BiupiuLearningRegistry is Ownable {
    struct LearningCheckpoint {
        bytes32 targetId;
        bytes32 modelVersion;
        bytes32 datasetManifestHash;
        bytes32 lineageRoot;
        bytes32 metricsHash;
        bytes32 policyHash;
        uint64 anchoredAt;
    }

    mapping(bytes32 => LearningCheckpoint) private _checkpoints;
    mapping(bytes32 => bool) public checkpointExists;

    error CheckpointAlreadyAnchored();
    error CheckpointNotFound();
    error InvalidHash();

    event LearningCheckpointAnchored(
        bytes32 indexed checkpointId,
        bytes32 indexed targetId,
        bytes32 modelVersion,
        bytes32 datasetManifestHash,
        bytes32 lineageRoot,
        bytes32 metricsHash,
        bytes32 policyHash,
        uint64 anchoredAt
    );

    constructor() Ownable(msg.sender) {}

    function anchorCheckpoint(
        bytes32 checkpointId,
        bytes32 targetId,
        bytes32 modelVersion,
        bytes32 datasetManifestHash,
        bytes32 lineageRoot,
        bytes32 metricsHash,
        bytes32 policyHash
    ) external onlyOwner {
        if (checkpointExists[checkpointId]) revert CheckpointAlreadyAnchored();
        if (
            targetId == bytes32(0)
            || modelVersion == bytes32(0)
            || datasetManifestHash == bytes32(0)
            || lineageRoot == bytes32(0)
            || metricsHash == bytes32(0)
            || policyHash == bytes32(0)
        ) revert InvalidHash();

        _checkpoints[checkpointId] = LearningCheckpoint({
            targetId: targetId,
            modelVersion: modelVersion,
            datasetManifestHash: datasetManifestHash,
            lineageRoot: lineageRoot,
            metricsHash: metricsHash,
            policyHash: policyHash,
            anchoredAt: uint64(block.timestamp)
        });
        checkpointExists[checkpointId] = true;

        emit LearningCheckpointAnchored(
            checkpointId,
            targetId,
            modelVersion,
            datasetManifestHash,
            lineageRoot,
            metricsHash,
            policyHash,
            uint64(block.timestamp)
        );
    }

    function getCheckpoint(bytes32 checkpointId)
        external
        view
        returns (LearningCheckpoint memory)
    {
        if (!checkpointExists[checkpointId]) revert CheckpointNotFound();
        return _checkpoints[checkpointId];
    }
}
