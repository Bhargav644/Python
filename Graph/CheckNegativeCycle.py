# O(VE)
# dynamic approach
# wroks for negative edges but not for neagative cycles
# as we know that in bellmanford algo we got all shortest path in V-1 steps
# but if it's distance is changing after V-1 steps that means we are facing negative cycles
infinity = int(1e6)
distance = {}


def CheckNegatoveCycle(edges, V, source):
    for i in range(V):
        distance[i] = infinity
    distance[source] = 0
    for i in range(V-1):  # becauz for 1st edge there can be V-1 paths
        for j in edges:
            distance[j[1]] = min(distance[j[1]], distance[j[2]]+j[0])
            # for undirected graph
            distance[j[2]] = min(distance[j[2]], distance[j[1]]+j[0])
    for i in range(1):
        for j in edges:
            before1 = distance[j[1]]
            before2 = distance[j[2]]
            distance[j[1]] = min(distance[j[1]], distance[j[2]]+j[0])
            # for undirected graph
            distance[j[2]] = min(distance[j[2]], distance[j[1]]+j[0])
            after1 = distance[j[1]]
            after2 = distance[j[2]]
            if(before1 != after1 or before2 != after2):
                return True
    return False


(V1, E1) = (9, 14)
edgesWithoutCycle = [(4, 0, 1), (8, 0, 7), (8, 1, 2), (11, 1, 7), (7, 2, 3), (2, 2, 8), (4, 2, 5),
                     (9, 3, 4), (14, 3, 5), (10, 4, 5), (2, 5, 6), (1, 6, 7), (6, 8, 6), (7, 8, 7)]  # (weights,x->y)
print(CheckNegatoveCycle(edgesWithoutCycle, V1, 0))
(V2, E2) = (4, 4)
edgesWithCycle = [(-1, 0, 1), (-10, 0, 2,), (5, 2, 3), (2, 1, 3)]
print(CheckNegatoveCycle(edgesWithCycle, V2, 0))
