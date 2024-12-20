def solution(n):
    tile = [0]*5001
    tile[2] = 3

    for i in range(4, 5001, 2):
        tile[i] = tile[2] * tile[i - 2]
        for j in range(4, i, 2):
            tile[i] += 2 * tile[i - j]
        tile[i] += 2 
    answer = tile[n] % 1000000007
    return answer