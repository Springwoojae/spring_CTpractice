import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

if n > m:
    print(n - m)
else:
    print(m - n)