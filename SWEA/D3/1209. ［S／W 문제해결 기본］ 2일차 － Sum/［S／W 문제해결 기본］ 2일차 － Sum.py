for test_case in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    di = [1, 1, -1]
    dj = [0, 1, 1]
    s_lst = []
    ans_rd = 0
    ans_ru = 0

    for i in range(100):
        ans = 0
        for j in range(100):
            ans += arr[i][j]
        s_lst.append(ans)

    for j in range(100):
        ans = 0
        for k in range(100):
            ni = di[0] * k
            nj = j + dj[0] * k
            if 0 <= ni < 100 and 0 <= nj < 100:
                ans += arr[ni][nj]
        s_lst.append(ans)

    for i in range(100):
        rdi = di[1] * i
        rdj = dj[1] * i
        rui = 99 + di[2] * i
        ruj = dj[2] * i
        if 0 <= rdi < 100 and 0 <= rdj < 100:
            ans_rd += arr[rdi][rdj]
        if 0 <= rui < 100 and 0 <= ruj < 100:
            ans_ru += arr[rui][ruj]
    s_lst.append(ans_rd)
    s_lst.append(ans_ru)

    ans = 0
    for i in s_lst:
        if ans < i:
            ans = i
    print(f'#{T} {ans}')