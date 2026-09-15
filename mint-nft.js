const hre = require("hardhat");
async function main() {
  const contractAddress = process.env.NFT_CONTRACT_ADDRESS;
  const recipient = process.env.RECIPIENT;
  const tokenURI = process.env.TOKEN_URI;
  if (!contractAddress || !recipient || !tokenURI) throw new Error("Set NFT_CONTRACT_ADDRESS, RECIPIENT and TOKEN_URI in .env");
  const nft = await hre.ethers.getContractAt("BiupiuNFT", contractAddress);
  const tx = await nft.mint(recipient, tokenURI);
  console.log(`tx=${tx.hash}`);
  const receipt = await tx.wait();
  console.log(`block=${receipt.blockNumber}`);
}
main().catch((e) => { console.error(e); process.exitCode = 1; });
