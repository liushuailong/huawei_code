import sys

def test(ctx):
    if ctx == 1:
        return 1
    if ctx == 2:
        return 1
    return test(ctx - 1) + test(ctx - 2)


for line in sys.stdin:
    a = line.strip()
    print(test(int(a)))