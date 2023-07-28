import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a + b)