import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
ans = []

for i in lst:
    if i < x:
        ans.append(str(i))

print(' '.join(ans))