import sys
sys.setrecursionlimit(100000)

n, m = map(int, sys.stdin.readline().rstrip().split())

parent = [i for i in range(n + 1)]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


for i in range(m):
    z, a, b = map(int, sys.stdin.readline().rstrip().split())
    if z == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')