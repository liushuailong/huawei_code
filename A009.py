import sys


def test(ctx):
    ctx = int(ctx)
    if ctx == 1 or ctx == 2:
        return -1
    ctx = ctx -3
    arr = [2, 3, 2, 4]
    return arr[ctx % 4]


for line in sys.stdin:
    a = line.strip()
    print(test(a))