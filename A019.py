import sys

row = 0
col = 0
def test(n, line):
    global row
    global col
    if n % 5 == 0:
        row, col = map(int, line.split(" "))
        if 0<=row<=9 and 0<=col<=9:
            print(0)
        else:
            print(-1)
    elif n%5 ==1:
        x1, y1, x2, y2 = map(int, line.split(" "))
        if 0<=x1<=row-1 and 0<=y1<=col-1 and 0<=x2<=row-1 and 0<=y2<=col-1:
            print(0)
        else:
            print(-1)
    elif n%5 ==2:
        x1 = int(line)
        if 0<=x1<=row-1 and row + 1 <=9:
            print(0)
        else:
            print(-1)
    elif n%5 == 3:
        x1 = int(line)
        if 0<=x1<=col-1 and col + 1 <=9:
            print(0)
        else:
            print(-1)
    elif n%5 == 4:
        x1, y1 = map(int, line.split(" "))
        if 0<=x1<=row-1 and 0<=y1<=col-1:
            print(0)
        else:
            print(-1)








for line in enumerate(sys.stdin):
    test(line[0], line[1].strip())

