a, b = map(int, input().split())
k, x = map(int, input().split())

result = 0
if a <= k + x <= b:
    if a <= k - x <= b:
        result = 2 * x + 1
    else:
        result = k + x - a + 1
else:
    if a <= k - x <= b:
        result = b - (k - x) + 1
    else:
        if k - x < a and k + x > b:
            result = b - a + 1
        else:
            result = 'IMPOSSIBLE'

print(result)