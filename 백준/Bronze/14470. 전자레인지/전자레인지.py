import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())
E = int(sys.stdin.readline().rstrip())

if A < 0:
    sec = ((-A) * C) + D + (B * E)
elif A > 0:
    sec = (B - A) * E
else:
    sec = D + B * E

print(sec)