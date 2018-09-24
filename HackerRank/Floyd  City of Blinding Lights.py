#https://www.hackerrank.com/challenges/floyd-city-of-blinding-lights

#!/bin/python3

import os
import sys



if __name__ == '__main__':

    road_nodes, road_edges = map(int, input().split())

    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges

    for road_itr in range(road_edges):
        road_from[road_itr], road_to[road_itr], road_weight[road_itr] = map(int, input().split())


    table=[]
    for i in range(0, road_nodes+1):
            line=[]
            for k in range(0, road_nodes+1):
                line.append(float('inf'))
            table.append( line )

    for i in range(1, road_nodes+1):
            table[i][i]=0

    for i in range( len(road_from)):
            table[ road_from[i] ][ road_to[i] ]=road_weight[i]


    for i in range (1, road_nodes+1):
        for k in range (1, road_nodes+1):
            for j in range (1, road_nodes+1):
                table[k][j]= min ( table[k][j], table[k][i]+table[i][j])


    q = int(input())

    for q_itr in range(q):
        xy = input().split()

        x = int(xy[0])

        y = int(xy[1])
        if ( table[x][y] != float('inf')):
            print(table[x][y])
        else:
            print( -1)
