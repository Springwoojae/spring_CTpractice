def solution(a, b):
    answer = 0
    i = 2 * a * b
    a = str(a)
    b = str(b)
    j = a + b
    j = int(j)
    if i > j:
        answer = i
    else:
        answer = j
    return answer