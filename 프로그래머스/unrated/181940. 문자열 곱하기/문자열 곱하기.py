def solution(my_string, k):
    answer = ''
    for j in range(k):
        for i in range(len(my_string)):
            answer = answer + my_string[i]
    return answer