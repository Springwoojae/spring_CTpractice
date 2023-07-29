import sys

N = int(sys.stdin.readline().rstrip())
name_lst = []
pfn_lst = []

for i in range(N):
    name = sys.stdin.readline().rstrip()
    name_lst.append(name[0])
for f in name_lst:
    c_f = name_lst.count(f)
    if c_f >= 5:
        pfn_lst.append(f)

lst = list(set(pfn_lst))
lst.sort()

if pfn_lst == []:
    print("PREDAJA")
else:
    print(''.join(lst))