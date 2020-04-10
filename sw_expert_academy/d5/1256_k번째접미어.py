import sys
sys.stdin = open("1256_input.txt")

for tc in range(int(input())):
    k = int(input())
    string = input()
    data = []
    for i in range(len(string)):
        data.append(string[i:])
    # print(data)
    data.sort()
    # print(data)
    print(f"#{tc + 1} {data[k - 1]}")