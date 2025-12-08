class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

    def set(self, x):
        root = self.find(x)
        return [i for i, parent in enumerate(self.parent) if self.find(parent) == root]



if __name__ == "__main__":
    ds = DSU(5) # Space with 10 items
    print(ds.parent)
    print(ds.rank)
    print(ds.set(0))

    ds.union(1, 0)
    print(ds.parent)
    print(ds.rank)
    print(ds.set(0))

    ds.union(1, 4)
    print(ds.parent)
    print(ds.rank)
    print(ds.set(0))
