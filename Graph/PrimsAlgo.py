# O(v^2)
# used for minimum spanning tree
# can be done by heaps which leads to O(vloge)
infinity = int(1e7)
weight = {}
parent = {}
visited = {}


def findMinimum(distance, V):
    minimum = infinity
    minIndex = -1
    for i in range(V):
        if(not visited[i] and weight[i] < minimum):
            minimum = weight[i]
            minIndex = i
    return minIndex


def PrimsAlgo(adjL, V):
    for i in range(V):
        (weight[i], parent[i], visited[i]) = (infinity, i, False)
    weight[0] = 0
    for i in range(V-1):
        minIndex = findMinimum(weight, V)  # gives index with minimum weight
        visited[minIndex] = True
        for j in adjL[minIndex]:
            if(not visited[j[0]] and weight[j[0]] > j[1]):
                weight[j[0]] = j[1]
                parent[j[0]] = minIndex
    return parent


(V, E) = (9, 14)
edges = [(4, 0, 1), (8, 0, 7), (8, 1, 2), (11, 1, 7), (7, 2, 3), (2, 2, 8), (4, 2, 5),
         (9, 3, 4), (14, 3, 5), (10, 4, 5), (2, 5, 6), (1, 6, 7), (6, 8, 6), (7, 8, 7)]  # (weights,x->y)
adjL = {}
for i in range(V):
    adjL[i] = []
for i in edges:  # making adjacency list of edges
    adjL[i[1]].append((i[2], i[0]))
    adjL[i[2]].append((i[1], i[0]))
print(PrimsAlgo(adjL, V))
cost = 0
for i in range(V):
    cost += weight[i]

print(cost)
