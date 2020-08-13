#!/bin/python3

import math
import os
import random
import re
import sys
import time
#import operator
def Prime(n):
    n = abs(n)
    if n == 1 :
        return "Not prime"
    elif (n == 2) or (n == 3) or (n == 5) or (n == 7):
        return "Prime"
    elif n % 2 == 0:
        return "Not prime"
    else:
        for i in range(3, int((math.sqrt(n)))+1, 2):
            if n % i == 0:
                return "Not prime"
    return "Prime"

if __name__ == '__main__':
    #r = operator.xor(17, 7)
    #print(r)
    a = 17
    b = 7
    print(a^b)