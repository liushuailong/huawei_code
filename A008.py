import sys

def test(ctx):
    ctx = ctx.replace("{", "(").replace("}", ")")
    ctx = ctx.replace("[", "(").replace("]", ")")
    return eval(ctx)


for line in sys.stdin:
    a = line.strip()
    print(test(a))