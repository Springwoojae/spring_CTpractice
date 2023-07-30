num = int(input())

for i in range(num):
    i = str(i)
    ans = ''
    ans_2 = 0
    for j in range(len(i)):
        ans += i[j]
        ans_2 += int(i[j])
    if int(ans) + ans_2 == num:
        print(ans)
        break
else:
    print(0)