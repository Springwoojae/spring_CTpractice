N = int(input())
nums = list(map(int, input().split()))

m = k = nums[0]

for i in nums:
    if i < m:
        m = i
    if i > k:
        k = i
print(m, k)