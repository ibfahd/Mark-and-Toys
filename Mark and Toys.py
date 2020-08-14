#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    toys = []
    toysprice = 0
    for p in prices:
        if p <= k:
            toysprice = toysprice + p
            if len(toys) == 0:
                toys.append(p)
            else:
                if len(toys) == 1:
                    if toys[0] > p:
                        toys.insert(0, p)
                    else:
                        toys.append(p)
                else:
                    if p >= toys[len(toys)-1]:
                        toys.append(p)
                    else:
                        for i in range(len(toys)-1,0,-1):
                            if p < toys[i] and p >= toys[i-1]:
                                toys.insert(i, p)
                                break
                            elif i == 1:
                                toys.insert(0, p)
                                break
            if toysprice > k:
                toysprice = toysprice - toys[len(toys)-1]
                toys.pop(len(toys)-1)
    print(toys)
    return len(toys)

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    print(result)
