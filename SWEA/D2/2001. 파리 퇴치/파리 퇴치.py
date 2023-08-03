T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 1]
    dj = [1, 0, 1]
    k_f = []

    for i in range(N):
        for j in range(N):
            kill_fly = 0
            for k in range(M):
                for l in range(M):
                    if 0 <= i+k < N and 0 <= j+l < N:
                        kill_fly += arr[i+k][j+l]
            k_f.append(kill_fly)

    k_m = 0
    for i in k_f:
        if k_m < i:
            k_m = i

    print(f'#{test_case} {k_m}')