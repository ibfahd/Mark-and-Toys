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
        ntoys = len(toys)
        if p <= k:
            toysprice = toysprice + p
            if ntoys == 0:
                toys.append(p)
            else:
                for i in range(ntoys-1,0,-1):
                    if p <= toys[i] and p >= toys[i-1]:
                        toys.insert(i, p)
                        break
                    else:
                        toys.insert(0, p)
            if toysprice > k:
                toysprice = toysprice - toys[ntoys]
                toys.pop(ntoys)
    return len(toys)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    fptr.write(str(result) + '\n')
    fptr.close()
