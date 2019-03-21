import sys
sys.stdin = open("5185_input.txt")

asc = [[0, 0, 0, 0],
       [0, 0, 0, 1],
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 1, 0, 0],
       [0, 1, 0, 1],
       [0, 1, 1, 0],
       [0, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 1],
       [1, 0, 1, 0],
       [1, 0, 1, 1],
       [1, 1, 0, 0],
       [1, 1, 0, 1],
       [1, 1, 1, 0],
       [1, 1, 1, 1]]

for tc in range(int(input())):
    n, data = input().split()
    n = int(n)
    result = []

    for i in data:
        if ord(i) >= 65:
            result += asc[ord(i) - 55]
        else:
            result += asc[int(i)]

    # print(n, data)
    print("#{}".format(tc + 1), ''.join(map(str, result)))