#https://www.hackerrank.com/challenges/unbounded-knapsack/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the unboundedKnapsack function below.



def solve(k, ind,arr,dp):
    if ind >= len(arr):
        return 0
    if k<=0:
        return 0
    if k%arr[ind]==0:
        return k
    if arr[ind] > k:
        return 0
    
    if k in dp:
        if ind in dp[k]:
            return dp[k][ind]
        
    res =   max(arr[ind]+solve(k-arr[ind], ind, arr,dp), arr[ind]+solve(k-arr[ind], ind+1, arr,dp), 0+solve(k, ind+1, arr,dp))
    if k not in dp:
        dp[k] = {}
        dp[k][ind] = res
    else:
        dp[k][ind] = res

    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    sys.setrecursionlimit(1000000)
    t = int(input())
    while t>0:
        
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
    
        dp = {}
        arr = list(map(int, input().rstrip().split()))
        arr.sort()
        result = solve(k, 0, arr,dp)

        fptr.write(str(result) + '\n')

       
        
        t-=1
    fptr.close()