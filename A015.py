import sys


def test(ctx):
    stack = []
    l = []
    counter = 0
    for i in ctx:
        if i == '"' in stack:
            l.append("".join(stack[1::]))
            stack = []
            counter += 1
        elif i == " " and '"' not in stack:
            if len(stack) != 0:
                l.append("".join(stack[0::]))
                stack = []
                counter += 1
        else:
            stack.append(i)
    if len(stack) != 0:
        l.append("".join(stack[0::]))
        counter += 1
    print(counter)
    for j in l:
        print(j)


for line in sys.stdin:
    test(line.strip())


