import sys

def test(num):

    # print(kong)
    # print("111111111111111")
    return int(num / 2 )


for line in sys.stdin:
    a = line.strip()
    # print(a)
    if a == "0":
        exit(0)
    else:
        print(test(int(a)))