#https://codeforces.com/problemset/problem/493/C


import collections
from collections import Counter
N1 = int (input())
team1 = list(map(int,input().split()))

N2 = int (input())
team2 = list(map(int,input().split()))

counts_t1=Counter(team1)
counts_t2=Counter(team2)

total={}

for i in team1:
    total[i]="t1"

for i in team2:
    if (i in total and total[i]=="t1"):
        total[i]="t3"
    else:
        total[i]="t2"

total = collections.OrderedDict(sorted(total.items()))
#print(total)

team1_tot=3*len(team1)
team2_tot=3*len(team2)

max_t1= team1_tot
max_t2= team2_tot
#print(team1_tot)
#print(team2_tot)
#print(max)


for bound in (total):
    #print( str(bound) +" "+ str(total[bound]) + str(str(total[bound]) == "t1"))
    if(str(total[bound]) == "t3"):
        team1_tot -= 1 *counts_t1[bound]
        team2_tot -= 1 * counts_t2[bound]

    if(str(total[bound]) == "t1"):
        team1_tot -= 1 * counts_t1[bound]

    if(str(total[bound]) == "t2"):
        team2_tot -= 1 * counts_t2[bound]

    #print(str(bound) + "  " +str(team1_tot) +" "+ str(team2_tot))
    if( team1_tot - team2_tot > max_t1 - max_t2 ):
        max_t1 = team1_tot
        max_t2 = team2_tot
    if ( (team1_tot - team2_tot == max_t1 - max_t2)  and (team1_tot > max_t1) ):
        max_t1 = team1_tot
        max_t2 = team2_tot


print(str(max_t1)+ ":"+ str(max_t2))
