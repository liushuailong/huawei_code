"""
描述
根据输入的日期，计算是这一年的第几天。
保证年份为4位数且日期合法。
进阶：时间复杂度：，空间复杂度：
输入描述：
输入一行，每行空格分割，分别是年，月，日

输出描述：
输出是这一年的第几天
"""
import sys



month_day = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def is_runian(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    return False


def test(year, month, day):
    res = 0
    for i in range(1, month):
        if i == 2:
            if is_runian(year):
                res += 29
            else:
                res += month_day[i]
            continue
        res += month_day[i]
    return res + day

for line in sys.stdin:
    print(test(*[int(i) for i in line.strip().split(" ")]))


