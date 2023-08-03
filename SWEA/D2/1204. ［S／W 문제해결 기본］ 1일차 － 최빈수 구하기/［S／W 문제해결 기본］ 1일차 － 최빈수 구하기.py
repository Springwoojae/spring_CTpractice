T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    A = [0] * 101
    idx = 0

    for i in lst:
        A[i] += 1

    for j in range(101):
        if A[j] >= idx:
            idx = A[j]
            ans = j
    print(f'#{test_case} {ans}')