import sys


def test(n):
    res = [str(i) for i in range(n * (n - 1) + 1, n * (n + 1)) if i % 2 != 0]
    print("+".join(res))


for line in sys.stdin:
    test(int(line.strip()))

