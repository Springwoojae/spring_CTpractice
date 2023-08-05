T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for i in range(N):
        con_box = 0
        for j in range(N):
            if arr[i][j] == 1:
                con_box += 1
            else:
                if con_box == K:
                    ans += 1
                con_box = 0
        if con_box == K:
            ans += 1

    for j in range(N):
        con_box = 0
        for i in range(N):
            if arr[i][j] == 1:
                con_box += 1
            else:
                if con_box == K:
                    ans += 1
                con_box = 0
        if con_box == K:
            ans += 1

    print(f'#{test_case} {ans}')