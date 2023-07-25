num = int(input())

for i in range(num):
    mark = list(input())
    M_R = int(len(mark) / 2)
    for j in range(M_R):
        if mark.count('(') == mark.count(')') and mark.index('(') < mark.index(')'):
            mark.remove('(')
            mark.remove(')')
    if len(mark) == 0:
        print('YES')
    else:
        print('NO')