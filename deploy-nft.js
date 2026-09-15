const hre = require("hardhat");
async function main() {
  const [deployer] = await hre.ethers.getSigners();
  const name = process.env.COLLECTION_NAME || "BIUPIU / ORIGIN";
  const symbol = process.env.COLLECTION_SYMBOL || "BIU";
  const maxSupply = BigInt(process.env.MAX_SUPPLY || "10000");
  const royaltyReceiver = process.env.ROYALTY_RECEIVER || deployer.address;
  const royaltyBps = Number(process.env.ROYALTY_BPS || "500");
  const Factory = await hre.ethers.getContractFactory("BiupiuNFT");
  const contract = await Factory.deploy(name, symbol, maxSupply, royaltyReceiver, royaltyBps);
  await contract.waitForDeployment();
  console.log(`BiupiuNFT=${await contract.getAddress()}`);
  console.log(`chainId=${(await hre.ethers.provider.getNetwork()).chainId}`);
}
main().catch((e) => { console.error(e); process.exitCode = 1; });
