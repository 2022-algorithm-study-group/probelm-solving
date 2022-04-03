import sys


input = sys.stdin.readline


TC = int(input())
REQUIRED_INK = 10 ** 6
for t in range(TC):
    res = []
    printers = [list(map(int, input().split())) for i in range(3)]
    for p in range(4):
        res.append(min(printers[0][p], printers[1][p], printers[2][p]))
    if sum(res) >= REQUIRED_INK:
        answer = REQUIRED_INK
        for i in range(4):
            min_value = min(answer, res[i])
            res[i] = min_value
            answer -= min_value
        print("Case #%d: %d %d %d %d" % (t + 1, res[0], res[1], res[2], res[3]))
    else:
        print("Case #%d: IMPOSSIBLE" % (t + 1))
