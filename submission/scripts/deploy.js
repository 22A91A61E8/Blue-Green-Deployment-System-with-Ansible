import { ethers } from "hardhat";

async function main() {

  const Faucet = await ethers.getContractFactory("TokenFaucet");
  const Token = await ethers.getContractFactory("YourToken");

  const faucet = await Faucet.deploy("TOKEN_ADDRESS_PLACEHOLDER");
  await faucet.waitForDeployment();

  const token = await Token.deploy(await faucet.getAddress());
  await token.waitForDeployment();

  console.log("Token deployed:", await token.getAddress());
  console.log("Faucet deployed:", await faucet.getAddress());
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});