
indegree = {}
adjL = {}


def TopologicalSort(adjL, v):
    list = []
    q = []
    for i in range(v):
        if(indegree[i] == 0):
            q.append(i)
    while(len(q) != 0):
        top = q.pop(0)
        list.append(top)
        indegree[top] -= 1
        for i in adjL[top]:
            indegree[i] -= 1
            if(indegree[i] == 0):
                q.append(i)

    return list


v, e = list(map(int, input().strip().split()))
for i in range(v):
    adjL[i] = []
    indegree[i] = 0
for i in range(e):
    x, y = list(map(int, input().strip().split()))
    adjL[x].append(y)
    # adjL[y].append(x)
    indegree[y] += 1
# adjL={0:[],1:[],2:[3],3:[1],4:[0,1],5:[2,0]}
print(TopologicalSort(adjL, v))
