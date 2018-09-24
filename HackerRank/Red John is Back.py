#https://www.hackerrank.com/challenges/red-john-is-back/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the redJohn function below.

def redJohn(n,d):
    if n<4:
        return 1
    if n in d:
        return d[n]


    result = redJohn(n-1,d) + redJohn(n-4,d)
    if n not in d:
        d[n]=result
    return result


def countP(M):
    counter=0
    if(M>=2):
        counter +=1
    for i in range(3, M+1, 2):
        flag=True
        for j in range(2, int(math.sqrt(i))+1):

            if(i%j==0):
                flag=False
        if flag:
            counter+=1

    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())
        d={}
        result = redJohn(n,d)
        result = countP(result)

        fptr.write(str(result) + '\n')

    fptr.close()
