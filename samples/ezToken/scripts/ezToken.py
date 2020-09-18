#!/usr/bin/python3

from brownie import Token, accounts


def main():
    tk = Token.deploy("Test Token", "TST", 18, 1e21, {'from': accounts[0]})
    ac0 = accounts[0]
    ac1 = accounts[1]
    ac2 = accounts[2]
    print(tk.balanceOf(ac0))
    print(tk.balanceOf(ac1))
    tk.transfer(ac1,5000,{'from':ac0})
    print(tk.balanceOf(ac0))
    print(tk.balanceOf(ac1))


