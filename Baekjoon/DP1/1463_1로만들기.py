import sys
sys.stdin = open("1463_input.txt")


def make_1(x):
    for i in range(4, x + 1):
        num1 = data[i - 1] + 1
        if not i % 2:
            num2 = data[i//2] + 1
        elif not i % 3:
            num2 = data[i//3] + 1
        else:
            num2 = num1
        data.append(min(num1, num2) + 1)

    return data[x]



x = int(input())
data = [0, 0, 1, 1]

print(make_1(x))
