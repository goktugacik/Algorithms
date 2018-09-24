#https://www.hackerrank.com/contests/algoritmos-2018-i-contest-1/challenges/sherlock-and-array

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    leng = len(arr)
    nos=arr

    for i in range(1,leng):
        nos[i] += nos[i-1]
    #print(nos)
    found=False
    if leng==1:
        found=True
        pass
    for i in range(1,leng-1):
        sum1=0
        sum2=0
        sum1=nos[i-1]
        sum2=nos[-1] - nos[i]
        if sum1==sum2:
            found=True
            break

    if found:
        return ("YES")
    else:
        return ("NO") 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
