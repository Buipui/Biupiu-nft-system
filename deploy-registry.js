const hre = require("hardhat");

async function main() {
  const Factory = await hre.ethers.getContractFactory("BiupiuResearchRegistry");
  const registry = await Factory.deploy();
  await registry.waitForDeployment();

  console.log(`BiupiuResearchRegistry=${await registry.getAddress()}`);
  console.log(`chainId=${(await hre.ethers.provider.getNetwork()).chainId}`);
}

main().catch((e) => {
  console.error(e);
  process.exitCode = 1;
});
