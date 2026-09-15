// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";

/// @title Biupiu Research Registry
/// @notice Prototype registry for anchoring approved research, algorithm and NFT release commitments.
/// @dev Stores identifiers and cryptographic commitments only; it does not publish confidential research or transfer IP.
contract BiupiuResearchRegistry is Ownable {
    struct ReleaseRecord {
        bytes32 researchId;
        bytes32 algorithmId;
        bytes32 algorithmVersion;
        bytes32 manifestHash;
        bytes32 provenanceHash;
        bytes32 standaloneHash;
        bytes32 metadataHash;
        address nftContract;
        uint256 tokenId;
        uint64 registeredAt;
        bool tokenLinked;
    }

    mapping(bytes32 => ReleaseRecord) private _releases;
    mapping(bytes32 => bool) public releaseExists;

    error ReleaseAlreadyRegistered();
    error ReleaseNotFound();
    error TokenAlreadyLinked();
    error ZeroAddress();

    event ReleaseRegistered(
        bytes32 indexed releaseId,
        bytes32 indexed researchId,
        bytes32 indexed algorithmId,
        bytes32 algorithmVersion,
        bytes32 manifestHash,
        bytes32 provenanceHash,
        bytes32 standaloneHash,
        bytes32 metadataHash,
        uint64 registeredAt
    );

    event TokenLinked(bytes32 indexed releaseId, address indexed nftContract, uint256 indexed tokenId);

    constructor() Ownable(msg.sender) {}

    /// @notice Anchor an approved release manifest and its paired asset commitments.
    /// @dev Call only after the off-chain IP/licence/release gate has approved publication.
    function registerRelease(
        bytes32 releaseId,
        bytes32 researchId,
        bytes32 algorithmId,
        bytes32 algorithmVersion,
        bytes32 manifestHash,
        bytes32 provenanceHash,
        bytes32 standaloneHash,
        bytes32 metadataHash
    ) external onlyOwner {
        if (releaseExists[releaseId]) revert ReleaseAlreadyRegistered();

        _releases[releaseId] = ReleaseRecord({
            researchId: researchId,
            algorithmId: algorithmId,
            algorithmVersion: algorithmVersion,
            manifestHash: manifestHash,
            provenanceHash: provenanceHash,
            standaloneHash: standaloneHash,
            metadataHash: metadataHash,
            nftContract: address(0),
            tokenId: 0,
            registeredAt: uint64(block.timestamp),
            tokenLinked: false
        });

        releaseExists[releaseId] = true;

        emit ReleaseRegistered(
            releaseId,
            researchId,
            algorithmId,
            algorithmVersion,
            manifestHash,
            provenanceHash,
            standaloneHash,
            metadataHash,
            uint64(block.timestamp)
        );
    }

    /// @notice Link a registered release to its minted NFT token after minting.
    function linkToken(bytes32 releaseId, address nftContract, uint256 tokenId) external onlyOwner {
        if (!releaseExists[releaseId]) revert ReleaseNotFound();
        if (nftContract == address(0)) revert ZeroAddress();
        ReleaseRecord storage record = _releases[releaseId];
        if (record.tokenLinked) revert TokenAlreadyLinked();

        record.nftContract = nftContract;
        record.tokenId = tokenId;
        record.tokenLinked = true;

        emit TokenLinked(releaseId, nftContract, tokenId);
    }

    function getRelease(bytes32 releaseId) external view returns (ReleaseRecord memory) {
        if (!releaseExists[releaseId]) revert ReleaseNotFound();
        return _releases[releaseId];
    }
}
