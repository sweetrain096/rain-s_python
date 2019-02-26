import sys
sys.stdin = open("1463_input.txt")


def make_1(x):
    for i in range(4, x + 1):
        data.append(data[i - 1] + 1)
        if not i % 2:
            data[i] = min(data[i], data[i//2] + 1)
        if not i % 3:
            data[i] = min(data[i], data[i // 3] + 1)

    return data[x]



x = int(input())
data = [0, 0, 1, 1]

print(make_1(x))
