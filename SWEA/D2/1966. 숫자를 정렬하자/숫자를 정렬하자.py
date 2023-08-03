T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for k in range(len(arr)):
        s_idx = k
        for i in range(k, len(arr)):
            if arr[s_idx] > arr[i]:
                s_idx = i
        arr[s_idx], arr[k] = arr[k], arr[s_idx]

    print(f'#{test_case}', *arr)