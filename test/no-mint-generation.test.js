const { expect } = require("chai");
const { ethers } = require("hardhat");

// These tests deliberately do not call mint(). They validate that the contracts
// can be generated/deployed locally and expose the expected empty initial state.
describe("No-mint contract generation smoke test", function () {
  it("deploys the artwork contract without creating an NFT", async function () {
    const [owner] = await ethers.getSigners();
    const Factory = await ethers.getContractFactory("BiupiuNFT");
    const contract = await Factory.deploy("BIU Artwork", "BIUART", 10, owner.address, 500);
    await contract.waitForDeployment();

    expect(await contract.totalMinted()).to.equal(0n);
    expect(await contract.maxSupply()).to.equal(10n);
  });

  it("deploys the certificate contract without creating a certificate", async function () {
    const [owner] = await ethers.getSigners();
    const Factory = await ethers.getContractFactory("BiupiuCertificate");
    const contract = await Factory.deploy("BIU Certificate", "BIUCOA", 10, owner.address, 500);
    await contract.waitForDeployment();

    expect(await contract.maxSupply()).to.equal(10n);
    expect(await contract.totalGovernanceWeight()).to.equal(0n);
  });

  it("deploys the provenance registry with no bonds or provenance records", async function () {
    const Factory = await ethers.getContractFactory("BiupiuProvenanceRegistry");
    const registry = await Factory.deploy();
    await registry.waitForDeployment();

    expect(await registry.bondExists(ethers.ZeroHash)).to.equal(false);
    expect(await registry.provenanceExists(ethers.ZeroHash)).to.equal(false);
  });
});
