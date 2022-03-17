# O(V^3)
# for finding shortest path of all nodes from single source
# dynamic approach
# does not work for negative cycles but works for negative edges and also used for negative cycle detection
import numpy as np
inf = int(1e6)

adjM = np.array([[0, 5, inf, 10],
                 [inf, 0, 3, inf],
                 [inf, inf, 0, 1],
                 [inf, inf, inf, 0]])


def FloydWarshallAlgo():
    v = len(adjM)
    for k in range(v):
        for i in range(v):
            for j in range(v):
                adjM[i][j] = min(adjM[i][j], adjM[i][k]+adjM[k][j])


FloydWarshallAlgo()
source = int(input())
destination = int(input())
print(adjM[source][destination])
