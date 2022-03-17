class Disjoint:
    parent = {}
    height = {}

    def __init__(self, V):
        for i in range(V):
            self.parent[i] = i
            self.height[i] = 0

    def findParent(self, child):
        if(self.parent[child] == child):
            return child
        self.parent[child] = self.findParent(self.parent[child])
        return self.parent[child]

    def Union(self, u, v):
        u = self.findParent(u)
        v = self.findParent(v)
        if(u != v):
            if(self.height[u] < self.height[v]):
                u, v = v, u
            if(self.height[u] == self.height[v]):
                self.height[u] += 1
            self.parent[v] = u


def KruskalAlgo(edges, V):
    cost = 0
    d = Disjoint(V)
    for e in edges:
        if(d.findParent(e[1]) != d.findParent(e[2])):
            d.Union(e[1], e[2])
            cost += e[0]
            print(e[1], '-', e[2], '\n')
    return cost


(V, E) = (9, 14)
edges = [(4, 0, 1), (8, 0, 7), (8, 1, 2), (11, 1, 7), (7, 2, 3), (2, 2, 8), (4, 2, 5),
         (9, 3, 4), (14, 3, 5), (10, 4, 5), (2, 5, 6), (1, 6, 7), (6, 8, 6), (7, 8, 7)]  # (weights,x->y)\
edges.sort()

print(KruskalAlgo(edges, V))
