import sys

def test(ctx):
    ctx = int(ctx)
    list1 = []
    list2 = []
    a = 0
    for i in range(1, ctx):
        a += i 
        if a > ctx:
            break
        else:
            if a % 10 == 6:
                list1.append(a)
            elif a % 100 == 28:
                list1.append(a)
    for x in list1:
        list3 = []
        for y in range(1, int(x/2+1)):
            if x % y == 0:
                list3.append(y)
        if sum(list3) == x:
            list2.append(x)
    return len(list2)

for line in sys.stdin:
    print(test(line.strip()))