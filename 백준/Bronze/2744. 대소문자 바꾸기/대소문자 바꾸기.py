import sys

str_1 = list(sys.stdin.readline().rstrip())
ans = []

for i in str_1:
    if i.isupper()== True:
        ans.append(i.lower())
    else:
        ans.append(i.upper())

print(''.join(ans))