#https://www.hackerrank.com/challenges/the-quickest-way-up/
#!/bin/python3
import collections

games = int ( input() )
jump={}
graph = {}
for i in range ( games ):
    #print("game",i)
    ldr = int ( input() )
    jump.clear()


    for i in range (ldr):
        fr, to= map(int,input().split())
        jump.update( {fr:to})

    snk= int ( input() )

    for i in range (snk):
        fr, to= map(int,input().split())
        jump.update( {fr:to})

    graph.clear()

    for k in range (1,101):
        graph.update ( {k:[]})

        for i in range (1,7):
            if k==100:
                break
            if k in jump:
                graph[ k ].append( jump.get(k) )
                break
            else:
                if not 100 in graph[k]:
                    graph[ k ].append( min (k+i,100) )
    #print(graph)
    visited = [False]*101
    distance = [ float('inf')]*101
    de = collections.deque()
    de.append(1)
    #print( graph[1])
    distance[1]=0
    found = False
    while ( de ):

        s = de.popleft()
        visited[s]=True


        for u in graph[s]:
            if visited[u]  :
                continue
            else:
                visited[u]=True
            if len(graph[s])>1 or u==99 :
                distance[u]= distance[s]+1
            else:
                distance[u]=distance[s]
            if u == 100:
                found = True
                break
            de.append(u)
    if found:
        print(distance[100])
        continue
    else:
        print(-1)    