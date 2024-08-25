arr = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
  arr[i] = int(input())

score = 0
pre_score = 0

for i in range(10):
  score += arr[i]
  if score < 100:
    pre_score = 100 - score
  elif score == 100:
    print(100)
    break
  else:
    if score - 100 <= pre_score:
      print(score)
    else:
      print(100-pre_score)
    break
  if i == 9:
    print(score)