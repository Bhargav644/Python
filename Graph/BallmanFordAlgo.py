# O(VE)
# dynamic approach
# wroks for negative edges but not for neagative cycles
infinity = int(1e6)
distance = {}


def BellmanFord(edges, V, source):
    for i in range(V):
        distance[i] = infinity
    distance[source] = 0
    for i in range(V-1):  # becauz for 1st edge there can be V-1 paths
        for j in edges:
            distance[j[1]] = min(distance[j[1]], distance[j[2]]+j[0])
            # for undirected graph
            distance[j[2]] = min(distance[j[2]], distance[j[1]]+j[0])
    return distance


(V, E) = (9, 14)
edges = [(4, 0, 1), (8, 0, 7), (8, 1, 2), (11, 1, 7), (7, 2, 3), (2, 2, 8), (4, 2, 5),
         (9, 3, 4), (14, 3, 5), (10, 4, 5), (2, 5, 6), (1, 6, 7), (6, 8, 6), (7, 8, 7)]  # (weights,x->y)
print(BellmanFord(edges, V, 0))
