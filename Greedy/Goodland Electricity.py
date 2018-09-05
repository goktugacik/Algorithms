#https://www.hackerrank.com/challenges/pylons/copy-from/77205895
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pylons function below.
def pylons(k, arr):
    
    ans=0
    is_lit = False
    error=False
    start = 0
    temp=-1
    while start<len(arr):
            is_lit = False
            j=start+k-1
            j= min(len(arr)-1, j)
            while(j>temp):
                if arr[j]==1:
                    temp=j
                    start = j+k
                    ans +=1
                    is_lit = True
                    break
                j-=1
            if not is_lit:
                error = True
                break

    if error:
        return(-1)
    else:
        return(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
