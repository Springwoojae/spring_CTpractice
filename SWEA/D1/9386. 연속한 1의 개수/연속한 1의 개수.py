T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num = input()

    max_1 = 0
    ans = 0

    for i in num:
        if int(i) == 1:
            max_1 += 1
            if max_1 > ans:
                ans = max_1
        else:
            max_1 = 0

    print(f'#{test_case} {ans}')