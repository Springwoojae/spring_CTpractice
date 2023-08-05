T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    arr = [2, 3, 5, 7, 11]
    arr_2 = []

    for i in arr:
        ans = 0
        while N % i == 0:
            N = N / i
            ans += 1
        arr_2.append(ans)
    print(f'#{test_case}', *arr_2)