import sys

while True:
    str_1 = sys.stdin.readline().rstrip()
    if bool(str_1) == False:
        break
    else:
        print(str_1)