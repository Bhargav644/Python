# O(V^2)
# for finding shortest path of all nodes from single source
# greedy approach
# does not work for negative cycles
infinity = int(1e6)
distance = {}


def DijkstraAlgo(adjL, V, source):
    for i in range(V):
        distance[i] = infinity
    distance[source] = 0
    list = [(0, source)]
    while(list != []):
        list.sort()
        top = list[0]
        list.remove(top)
        weight = top[0]
        vertex = top[1]
        for i in adjL[vertex]:  # ................................... 2
            if(distance[i[0]] > distance[vertex]+i[1]):   # A[1]-------B[4]  4 > 1+2
                if(distance[i[0]] != infinity):
                    list.remove((distance[i[0]], i[0]))
                distance[i[0]] = distance[vertex]+i[1]
                list.append((distance[i[0]], i[0]))
    return distance


(V, E) = (9, 14)
edges = [(4, 0, 1), (8, 0, 7), (8, 1, 2), (11, 1, 7), (7, 2, 3), (2, 2, 8), (4, 2, 5),
         (9, 3, 4), (14, 3, 5), (10, 4, 5), (2, 5, 6), (1, 6, 7), (6, 8, 6), (7, 8, 7)]  # (weights,x->y)
adjL = {}
for i in range(V):
    adjL[i] = []
for i in edges:  # making adjacency list of edges
    adjL[i[1]].append((i[2], i[0]))
    adjL[i[2]].append((i[1], i[0]))
print(DijkstraAlgo(adjL, V, 0))
