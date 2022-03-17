indegree = {}
longestPath = {}
adjL = {}


def LongestPath(adjL, v):
    q = []
    for i in range(v):
        if(indegree[i] == 0):
            q.append(i)
    while(len(q) != 0):
        top = q.pop(0)
        indegree[top] -= 1
        for i in adjL[top]:
            indegree[i] -= 1
            longestPath[i] = max(longestPath[i], longestPath[top]+1)
            if(indegree[i] == 0):
                q.append(i)

    return longestPath


v, e = list(map(int, input().strip().split()))  # vertices and edges
for i in range(v):
    adjL[i] = []
    indegree[i] = 0
    longestPath[i] = 0
for i in range(e):
    x, y = list(map(int, input().strip().split()))  # x->y edge
    adjL[x].append(y)
    # adjL[y].append(x)
    indegree[y] += 1
# adjL={0:[],1:[],2:[3],3:[1],4:[0,1],5:[2,0]}
print(LongestPath(adjL, v))
