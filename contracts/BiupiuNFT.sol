// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {ERC721URIStorage} from "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import {ERC2981} from "@openzeppelin/contracts/token/common/ERC2981.sol";
import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import {IERC165} from "@openzeppelin/contracts/utils/introspection/IERC165.sol";

/// @title Biupiu NFT
/// @notice Controlled ERC-721 minting contract for the Biupiu research-to-art collection.
/// @dev Per-token metadata is fixed at mint time. Underlying Biupiu IP is not transferred by token ownership.
contract BiupiuNFT is ERC721URIStorage, ERC2981, Ownable {
    uint256 public immutable maxSupply;
    uint256 private _nextTokenId = 1;

    error MaxSupplyExceeded();
    error InvalidRoyaltyBps();
    error ZeroAddress();

    event BiupiuMinted(address indexed to, uint256 indexed tokenId, string tokenURI);

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 maxSupply_,
        address royaltyReceiver_,
        uint96 royaltyBps_
    ) ERC721(name_, symbol_) Ownable(msg.sender) {
        if (maxSupply_ == 0) revert MaxSupplyExceeded();
        if (royaltyReceiver_ == address(0)) revert ZeroAddress();
        if (royaltyBps_ > 1000) revert InvalidRoyaltyBps(); // 10% ceiling for this reference contract

        maxSupply = maxSupply_;
        _setDefaultRoyalty(royaltyReceiver_, royaltyBps_);
    }

    /// @notice Mint a single NFT. Only the collection owner may mint.
    /// @dev The URI is stored directly on-chain as the token URI reference and cannot be edited later.
    function mint(address to, string calldata tokenURI_) external onlyOwner returns (uint256 tokenId) {
        if (to == address(0)) revert ZeroAddress();
        if (_nextTokenId > maxSupply) revert MaxSupplyExceeded();

        tokenId = _nextTokenId++;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI_);

        emit BiupiuMinted(to, tokenId, tokenURI_);
    }

    /// @notice Mint multiple NFTs with independent metadata URIs.
    function mintBatch(address[] calldata recipients, string[] calldata tokenURIs)
        external
        onlyOwner
        returns (uint256 firstTokenId, uint256 lastTokenId)
    {
        if (recipients.length == 0 || recipients.length != tokenURIs.length) revert MaxSupplyExceeded();
        if (_nextTokenId + recipients.length - 1 > maxSupply) revert MaxSupplyExceeded();

        firstTokenId = _nextTokenId;
        for (uint256 i = 0; i < recipients.length; ++i) {
            if (recipients[i] == address(0)) revert ZeroAddress();
            uint256 tokenId = _nextTokenId++;
            _safeMint(recipients[i], tokenId);
            _setTokenURI(tokenId, tokenURIs[i]);
            emit BiupiuMinted(recipients[i], tokenId, tokenURIs[i]);
            lastTokenId = tokenId;
        }
    }

    /// @notice Update the collection-wide royalty signal under ERC-2981.
    function setDefaultRoyalty(address receiver, uint96 feeNumerator) external onlyOwner {
        if (receiver == address(0)) revert ZeroAddress();
        if (feeNumerator > 1000) revert InvalidRoyaltyBps();
        _setDefaultRoyalty(receiver, feeNumerator);
    }

    /// @notice Remove the default royalty configuration.
    function deleteDefaultRoyalty() external onlyOwner {
        _deleteDefaultRoyalty();
    }

    function totalMinted() external view returns (uint256) {
        return _nextTokenId - 1;
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721URIStorage, ERC2981)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
