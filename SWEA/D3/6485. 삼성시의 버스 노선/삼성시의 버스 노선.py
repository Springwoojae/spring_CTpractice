T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    b_s = [0] * 5000
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A - 1, B):
            b_s[j] += 1
    P = int(input())
    C = [int(input()) for _ in range(P)]

    ans = []
    for i in C:
        ans.append(b_s[i - 1])

    print(f'#{test_case}', *ans)