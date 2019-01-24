import sys
sys.stdin = open("sample1_input.txt")

for t in range(int(input())):
    color_list = [[0 for i in range(10)] for i in range(10)]
    for n in range(int(input())):
        r1, c1, r2, c2, color = list(map(int, input().split()))
        purple = 0
        for row in range(r1 , r2 + 1):
            for col in range(c1, c2 + 1):
                color_list[row][col] += color
        for row in range(len(color_list)):
            for col in range(len(color_list[row])):
                if color_list[row][col] == 3:
                    purple += 1


    print(f"#{t + 1} {purple}")
