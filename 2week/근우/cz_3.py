import sys


input = sys.stdin.readline


TC = int(input())
for t in range(TC):
    dice_num = int(input())
    dices = list(map(int, input().split()))
    dices.sort()
    res = 1
    for i in range(dice_num):
        if dices[i] >= res:
            res += 1
    print("Case #%d: %d" % (t + 1, res - 1))
