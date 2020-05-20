#!/bin/python3

import math
import os
import random
import re
import sys

def par(valor):
    return valor % 2 == 0


if __name__ == '__main__':
    n = int(input().strip())
    if not par(n) or par(n) and n in range(6, 20 + 1):
        print("Weird")
    elif par(n) and n in range(2,5) or n > 20 and par(n):
        print("Not Weird")
