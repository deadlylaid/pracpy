v,e,start=map(int,input().split())

graph=[[] for i in range(v+1)]
check=[0 for d in range(v+1)]
for i in range(1,e+1):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for i in range(1,v+1):
    graph[t].sort()
