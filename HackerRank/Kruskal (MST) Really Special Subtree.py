#https://www.hackerrank.com/challenges/kruskalmstrsub/problem
#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
def find(u):
    if dad[u]==u:
        return u

    dad[u] = find ( dad[u])
    return dad[u]

if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().split())

    roads = []
    fro=[]
    to=[]
    cost=[]
    for _ in range(g_edges):
            roads=(list(map(int, input().rstrip().split())))
            fro.append(roads[0])
            to.append(roads[1])
            cost.append(roads[2])



    graph=[]

    for i in range(len(fro)):
        tup2 = ( cost[i] , (fro[i],to[i] ))
        bisect.insort( graph,  tup2 )


    #print(graph)
    visited = [False]*( (g_nodes))

    dad=[]
    for i in range (0, g_nodes+1 ):
        dad.append(i)
    #print(dad)
    cnt =0
    ans =0

    cnt +=1
    ans +=( graph[0][0] )
    dad [graph[0][1][1]] = dad[graph[0][1][0]]

    del graph[0]

    #print(graph)
    #print(dad)
    while cnt < g_nodes and len(graph)>0:
        cost = graph[0][0]
        u = graph[0][1][1]
        w = graph[0][1][0]

        if find(u)!=find(w):
            dad[ find(u) ] = dad [find(w)  ]
            cnt +=1
            ans += cost

        del graph[0]

    print(ans)