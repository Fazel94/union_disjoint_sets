from collections import Counter
# import time
import sys

# t = time.time()


class UnionFind:
    def __init__(self, size):
        self.rank = [0] * size
        self.p = [i for i in range(size)]

    def find_set(self, i):
        if self.p[i] == i:
            return i
        else:
            self.p[i] = self.find_set(self.p[i])
            return self.p[i]

    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)

    def union_set(self, i, j):
        if not self.is_same_set(i, j):
            x, y = self.find_set(i), self.find_set(j)
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1


n, m = map(int, sys.stdin.readline().strip().split())
union_find = UnionFind(n)
for i in range(m):
    k, *group = list(map(int, sys.stdin.readline().strip().split()))
    if k == 0 or k == 1:
        continue
    first = group[0] - 1
    for j in group[1:]:
        # groups[first].append(j - 1)
        # groups[j - 1].append(first)
        union_find.union_set(first, j - 1)

counts = Counter()
results = [0] * n
for i in range(n):
    result = union_find.find_set(i)
    counts[result] += 1
    results[i] = result
s = " ".join(map(str, map(lambda x: counts[x], results)))
# if n == 250000 and m == 250000:
# print(time.time() - t)
sys.stdout.write(s)
