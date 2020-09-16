#!/usr/bin/python3

from brownie import ezToken, accounts


def main():
    return ezToken.deploy({'from': accounts[0]})
