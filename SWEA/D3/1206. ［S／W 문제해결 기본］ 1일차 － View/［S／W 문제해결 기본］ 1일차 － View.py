T = 10
for test_case in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    lst_d = []
    for i in range(len(lst)):
        if lst[i] > 0:
            for j in range(i-2, i+3):
                if j == i:
                    pass
                elif lst[i] <= lst[j]:
                    lst_d.clear()
                    break
                else:
                    lst_d.append(lst[i] - lst[j])
            if len(lst_d) != 0:
                ans += min(lst_d)
                lst_d.clear()
    print(f'#{test_case} {ans}')