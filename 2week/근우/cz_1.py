import sys


input = sys.stdin.readline

total = int(input())

for i in range(total):
    r, c = map(int, input().split())
    res = []
    for j in range(2 * r + 1):
        cur = "+-" * c + "+" if j % 2 == 0 else "|." * c + "|"
        res.append(list(cur))
    res[0][0] = "."
    res[0][1] = "."
    res[1][0] = "."
    res = ["".join(c) for c in res]
    print("Case #%d:" % (i + 1))
    for c in res:
        print(c)
