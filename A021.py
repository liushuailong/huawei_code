import sys


def test(txt):
    print(sum([1 if "A" <= i <= "Z" else 0 for i in list(txt)]))


for line in sys.stdin:
    test(line.strip())

