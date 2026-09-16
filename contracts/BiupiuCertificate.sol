// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {ERC721URIStorage} from "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import {ERC2981} from "@openzeppelin/contracts/token/common/ERC2981.sol";
import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import {IERC165} from "@openzeppelin/contracts/utils/introspection/IERC165.sol";

/// @title Biupiu Certificate of Authenticity
/// @notice Standalone certificate NFT paired with artwork. Can be held, traded, and burned independently.
/// @dev Implements governance voting weight and burnable mechanism for dual-asset model.
contract BiupiuCertificate is ERC721URIStorage, ERC2981, Ownable {
    uint256 public immutable maxSupply;
    uint256 private _nextTokenId = 1;

    // Dual-asset bonding
    struct CertificateBond {
        address artworkContract;
        uint256 artworkTokenId;
        bytes32 proofHash;
        uint64 bondedAt;
        bool active;
    }

    mapping(uint256 => CertificateBond) public bonds;
    mapping(uint256 => bool) public burned;

    // Governance
    mapping(uint256 => uint256) public governanceWeight; // 1 vote per certificate
    uint256 public totalGovernanceWeight;

    error MaxSupplyExceeded();
    error InvalidRoyaltyBps();
    error ZeroAddress();
    error BondAlreadyExists();
    error BondNotFound();
    error TokenAlreadyBurned();
    error Unauthorized();

    event CertificateMinted(
        address indexed to,
        uint256 indexed tokenId,
        string tokenURI,
        bytes32 proofHash
    );
    event BondCreated(
        uint256 indexed certTokenId,
        address indexed artworkContract,
        uint256 indexed artworkTokenId,
        bytes32 proofHash
    );
    event CertificateBurned(uint256 indexed tokenId, address indexed burner);
    event GovernanceVote(
        uint256 indexed certTokenId,
        string indexed proposalId,
        bool support
    );

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 maxSupply_,
        address royaltyReceiver_,
        uint96 royaltyBps_
    ) ERC721(name_, symbol_) Ownable(msg.sender) {
        if (maxSupply_ == 0) revert MaxSupplyExceeded();
        if (royaltyReceiver_ == address(0)) revert ZeroAddress();
        if (royaltyBps_ > 1000) revert InvalidRoyaltyBps(); // 10% ceiling

        maxSupply = maxSupply_;
        _setDefaultRoyalty(royaltyReceiver_, royaltyBps_);
    }

    /// @notice Mint a single certificate with proof hash
    function mint(
        address to,
        string calldata tokenURI_,
        bytes32 proofHash_
    ) external onlyOwner returns (uint256 tokenId) {
        if (to == address(0)) revert ZeroAddress();
        if (_nextTokenId > maxSupply) revert MaxSupplyExceeded();

        tokenId = _nextTokenId++;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI_);
        governanceWeight[tokenId] = 1;
        totalGovernanceWeight += 1;

        emit CertificateMinted(to, tokenId, tokenURI_, proofHash_);
    }

    /// @notice Create dual-asset bond between certificate and artwork
    function bondToArtwork(
        uint256 certTokenId,
        address artworkContract,
        uint256 artworkTokenId,
        bytes32 proofHash_
    ) external onlyOwner {
        if (!_exists(certTokenId)) revert BondNotFound();
        if (bonds[certTokenId].active) revert BondAlreadyExists();
        if (artworkContract == address(0)) revert ZeroAddress();

        bonds[certTokenId] = CertificateBond({
            artworkContract: artworkContract,
            artworkTokenId: artworkTokenId,
            proofHash: proofHash_,
            bondedAt: uint64(block.timestamp),
            active: true
        });

        emit BondCreated(certTokenId, artworkContract, artworkTokenId, proofHash_);
    }

    /// @notice Burn certificate, revoking authenticity proof
    function burn(uint256 tokenId) external {
        if (!_isApprovedOrOwner(msg.sender, tokenId)) revert Unauthorized();
        if (burned[tokenId]) revert TokenAlreadyBurned();

        burned[tokenId] = true;
        if (bonds[tokenId].active) {
            bonds[tokenId].active = false;
        }
        if (governanceWeight[tokenId] > 0) {
            totalGovernanceWeight -= governanceWeight[tokenId];
            governanceWeight[tokenId] = 0;
        }

        _burn(tokenId);
        emit CertificateBurned(tokenId, msg.sender);
    }

    /// @notice Record governance vote (certificate holder voting)
    function vote(
        uint256 certTokenId,
        string calldata proposalId,
        bool support
    ) external {
        if (ownerOf(certTokenId) != msg.sender) revert Unauthorized();
        if (burned[certTokenId]) revert TokenAlreadyBurned();
        emit GovernanceVote(certTokenId, proposalId, support);
    }

    /// @notice Get certificate bond details
    function getBond(uint256 certTokenId)
        external
        view
        returns (CertificateBond memory)
    {
        if (!_exists(certTokenId)) revert BondNotFound();
        return bonds[certTokenId];
    }

    /// @notice Update collection-wide royalty
    function setDefaultRoyalty(address receiver, uint96 feeNumerator)
        external
        onlyOwner
    {
        if (receiver == address(0)) revert ZeroAddress();
        if (feeNumerator > 1000) revert InvalidRoyaltyBps();
        _setDefaultRoyalty(receiver, feeNumerator);
    }

    /// @notice Required by ERC165
    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721URIStorage, ERC2981)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
