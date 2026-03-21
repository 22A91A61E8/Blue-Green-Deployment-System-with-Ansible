// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IToken {
    function mint(address to, uint256 amount) external;
}

contract TokenFaucet {

    IToken public token;

    uint256 public constant FAUCET_AMOUNT = 10 * 10**18;
    uint256 public constant COOLDOWN_TIME = 24 hours;
    uint256 public constant MAX_CLAIM = 100 * 10**18;

    address public admin;
    bool public paused;

    mapping(address => uint256) public lastClaimAt;
    mapping(address => uint256) public totalClaimed;

    event TokensClaimed(address indexed user,uint256 amount,uint256 timestamp);

    constructor(address tokenAddress){
        token = IToken(tokenAddress);
        admin = msg.sender;
    }

    function requestTokens() external {

        require(!paused,"Faucet paused");
        require(canClaim(msg.sender),"Cooldown active");
        require(remainingAllowance(msg.sender) >= FAUCET_AMOUNT,"Lifetime limit reached");

        lastClaimAt[msg.sender] = block.timestamp;
        totalClaimed[msg.sender] += FAUCET_AMOUNT;

        token.mint(msg.sender,FAUCET_AMOUNT);

        emit TokensClaimed(msg.sender,FAUCET_AMOUNT,block.timestamp);
    }

    function canClaim(address user) public view returns(bool){
        return block.timestamp >= lastClaimAt[user] + COOLDOWN_TIME;
    }

    function remainingAllowance(address user) public view returns(uint256){

        if(totalClaimed[user] >= MAX_CLAIM){
            return 0;
        }

        return MAX_CLAIM - totalClaimed[user];
    }
}