T = int(input())
for test_case in range(1, 1 + T):
    sdk = [list(map(int, input().split())) for _ in range(9)]

    ans = 1

    # 가로 확인
    for i in range(9):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            try:
                nums.remove(sdk[i][j])
            except:
                ans = 0
    # 세로 확인
    for j in range(9):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(9):
            try:
                nums.remove(sdk[i][j])
            except:
                ans = 0
    # 박스 확인
    for p in range(3):
        for q in range(3):
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for i in range(3):
                for j in range(3):
                    try:
                        nums.remove(sdk[i][j])
                    except:
                        ans = 0
    print(f'#{test_case} {ans}')