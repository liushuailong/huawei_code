import sys

def test(ctx):
    count_list = set()
    for c in ctx:
        count_list.add((c, ctx.count(c)))
    count_list = list(count_list)
    count_list.sort(key=lambda x: x[1])
    last_c = None
    for k, v in count_list:
        if not last_c:
            last_c = v
        if last_c == v:
            ctx = ctx.replace(k, "")
    return ctx


for line in sys.stdin:
    a = line.strip()
    # print(a)
    if a == "0":
        exit(0)
    else:
        print(test(a))