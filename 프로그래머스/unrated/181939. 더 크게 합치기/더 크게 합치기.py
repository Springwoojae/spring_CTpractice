def solution(a, b):
    answer = 0
    a = str(a)
    b = str(b)
    i = a + b
    j = b + a
    if int(i) > int(j):
        answer = int(i)
    else:
        answer = int(j)
    return answer