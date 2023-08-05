T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))

    f_c = 0
    c_c = 0
    ans = 0

    for i in range(len(C)):
        if f_c <= C[i]:
            c_c += 1
            f_c = C[i]
            if ans < c_c:
                ans = c_c
        else:
            c_c = 0
            f_c = 0
            c_c += 1
            f_c = C[i]
            if ans < c_c:
                ans = c_c

    print(f'#{test_case} {ans}')