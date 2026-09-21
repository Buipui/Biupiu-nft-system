// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {ERC721} from "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import {ERC721URIStorage} from "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import {ERC2981} from "@openzeppelin/contracts/token/common/ERC2981.sol";
import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";

/// @title Biupiu Certificate of Authenticity
/// @notice Standalone certificate NFT paired with artwork. Can be held, traded, and burned independently.
/// @dev Experimental dual-asset certificate design. Validate thoroughly before deployment.
contract BiupiuCertificate is ERC721URIStorage, ERC2981, Ownable {
    uint256 public immutable maxSupply;
    uint256 private _nextTokenId = 1;

    struct CertificateBond {
        address artworkContract;
        uint256 artworkTokenId;
        bytes32 proofHash;
        uint64 bondedAt;
        bool active;
    }

    mapping(uint256 => CertificateBond) public bonds;
    mapping(uint256 => bool) public burned;
    mapping(uint256 => uint256) public governanceWeight;
    uint256 public totalGovernanceWeight;

    error MaxSupplyExceeded();
    error InvalidRoyaltyBps();
    error ZeroAddress();
    error BondAlreadyExists();
    error BondNotFound();
    error TokenAlreadyBurned();
    error Unauthorized();

    event CertificateMinted(address indexed to, uint256 indexed tokenId, string tokenURI, bytes32 proofHash);
    event BondCreated(uint256 indexed certTokenId, address indexed artworkContract, uint256 indexed artworkTokenId, bytes32 proofHash);
    event CertificateBurned(uint256 indexed tokenId, address indexed burner);
    event GovernanceVote(uint256 indexed certTokenId, string proposalId, bool support);

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 maxSupply_,
        address royaltyReceiver_,
        uint96 royaltyBps_
    ) ERC721(name_, symbol_) Ownable(msg.sender) {
        if (maxSupply_ == 0) revert MaxSupplyExceeded();
        if (royaltyReceiver_ == address(0)) revert ZeroAddress();
        if (royaltyBps_ > 1000) revert InvalidRoyaltyBps();
        maxSupply = maxSupply_;
        _setDefaultRoyalty(royaltyReceiver_, royaltyBps_);
    }

    function mint(address to, string calldata tokenURI_, bytes32 proofHash_)
        external
        onlyOwner
        returns (uint256 tokenId)
    {
        if (to == address(0)) revert ZeroAddress();
        if (_nextTokenId > maxSupply) revert MaxSupplyExceeded();
        tokenId = _nextTokenId++;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI_);
        governanceWeight[tokenId] = 1;
        totalGovernanceWeight += 1;
        emit CertificateMinted(to, tokenId, tokenURI_, proofHash_);
    }

    function bondToArtwork(
        uint256 certTokenId,
        address artworkContract,
        uint256 artworkTokenId,
        bytes32 proofHash_
    ) external onlyOwner {
        if (!_certificateExists(certTokenId)) revert BondNotFound();
        if (bonds[certTokenId].active) revert BondAlreadyExists();
        if (artworkContract == address(0)) revert ZeroAddress();
        bonds[certTokenId] = CertificateBond(artworkContract, artworkTokenId, proofHash_, uint64(block.timestamp), true);
        emit BondCreated(certTokenId, artworkContract, artworkTokenId, proofHash_);
    }

    function burn(uint256 tokenId) external {
        address tokenOwner = _requireOwned(tokenId);
        if (!_isAuthorized(tokenOwner, msg.sender, tokenId)) revert Unauthorized();
        if (burned[tokenId]) revert TokenAlreadyBurned();
        burned[tokenId] = true;
        bonds[tokenId].active = false;
        if (governanceWeight[tokenId] > 0) {
            totalGovernanceWeight -= governanceWeight[tokenId];
            governanceWeight[tokenId] = 0;
        }
        _burn(tokenId);
        emit CertificateBurned(tokenId, msg.sender);
    }

    function vote(uint256 certTokenId, string calldata proposalId, bool support) external {
        if (ownerOf(certTokenId) != msg.sender) revert Unauthorized();
        if (burned[certTokenId]) revert TokenAlreadyBurned();
        emit GovernanceVote(certTokenId, proposalId, support);
    }

    function getBond(uint256 certTokenId) external view returns (CertificateBond memory) {
        if (!_certificateExists(certTokenId)) revert BondNotFound();
        return bonds[certTokenId];
    }

    function setDefaultRoyalty(address receiver, uint96 feeNumerator) external onlyOwner {
        if (receiver == address(0)) revert ZeroAddress();
        if (feeNumerator > 1000) revert InvalidRoyaltyBps();
        _setDefaultRoyalty(receiver, feeNumerator);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721URIStorage, ERC2981)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }

    function _certificateExists(uint256 tokenId) internal view returns (bool) {
        return _ownerOf(tokenId) != address(0);
    }
}
