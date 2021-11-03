import sys
def test(str1, str2):
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    max_length = 0
    i = 0
    while i + max_length < len(str1):
        while i + max_length < len(str1) and str1[i:i + max_length + 1] in str2:
            max_length += 1
        i += 1
    return max_length

list_t = []
for line in sys.stdin:
    list_t.append(line.strip())
print(test(*list_t))

