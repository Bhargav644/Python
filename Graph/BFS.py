from collections import deque


def BFS(adjL, V):
    list = []
    visited = {}
    for i in range(V):
        visited[i] = False
    q = deque()
    q.append(2)
    while(len(q) != 0):
        front = q.popleft()
        if(not visited[front]):
            list.append(front)
            for i in adjL[front]:
                if(not visited[i]):
                    q.append(i)
            visited[front] = True
    return list


(v, e) = list(map(int, input().strip().split()))
adjL = {}
for i in range(v):
    adjL[i] = []
for i in range(e):
    x, y = list(map(int, input().strip().split()))
    adjL[x].append(y)
    # adjL[y].append(x) #for undirected graph
print(BFS(adjL, v))
