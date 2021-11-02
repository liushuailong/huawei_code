import sys

def test(ctx):
    for c in ctx:
        if not ("A" <= c <= "Z" or "a" <= c <= "z"):
            ctx = ctx.replace(c, " ")
    return " ".join(ctx.split()[::-1])


for line in sys.stdin:
    a = line.strip()
    print(test(a))