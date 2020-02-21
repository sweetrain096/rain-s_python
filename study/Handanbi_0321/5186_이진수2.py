import sys
sys.stdin = open("5186_input.txt")

for tc in range(int(input())):
    data = float(input())
    result = ""
    for i in range(13):
        data *= 2
        if data == 1:
            result += '1'
            break
        elif data > 1:
            result += '1'
            data -= 1
        else:
            result += '0'

    if data != 1.0:
        result = 'overflow'

    print("#{} {}".format(tc + 1, result))