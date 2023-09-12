h, m = map(int, input().split())
n = int(input())

t = h * 60 + m + n

h = t // 60
m = t % 60
if t // 60 >= 24:
    h = t // 60 - 24

print(h, m)