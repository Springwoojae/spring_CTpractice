for tc in range(1, int(input()) + 1):
    str_1 = input()

    st = 1
    ans = 1
    for i in range(1, len(str_1)):
        if str_1[i] == '(':
            st += 1
            ans += 1
        elif str_1[i] == ')':
            if str_1[i - 1] == '(':
                st -= 1
                ans += st - 1
            elif str_1[i - 1] == ')':
                st -= 1
    print(f'#{tc} {ans}')