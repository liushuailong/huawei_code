"""
描述
公元前五世纪，我国古代数学家张丘建在《算经》一书中提出了“百鸡问题”：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
现要求你打印出所有花一百元买一百只鸡的方式。
输入描述：
输入任何一个整数，即可运行程序。

输出描述：
 输出有数行，每行三个整数，分别代表鸡翁，母鸡，鸡雏的数量
"""


import sys

def test(ctx):
    for x in range(0, 20):
        if (100 - 7*x) % 4 == 0:
            y = int((100 - 7*x) / 4)
            if y < 0:
                continue
            z = 100 - x -y
            print("{} {} {}".format(x, y, z))
for line in sys.stdin:
    test(line.strip())
