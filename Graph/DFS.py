visited = {}
flag = False


def DFS(adjL, node):
    if(not visited[node]):
        visited[node] = True
        print(node)
    for i in adjL[node]:
        if(not visited[i]):
            DFS(adjL, i)


(v, e) = list(map(int, input().strip().split()))
for i in range(v):
    visited[i] = False
adjL = {}
for i in range(v):
    adjL[i] = []
for i in range(e):
    x, y = list(map(int, input().strip().split()))
    adjL[x].append(y)
    # adjL[y].append(x) #for undirected graph
DFS(adjL, 0)
