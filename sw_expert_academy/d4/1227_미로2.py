import sys
sys.stdin = open("1227_input.txt")




for tc in range(10):
    case_num = int(input())
    maze = []
    start, end = [], []
    for i in range(100):
        tmp = []
        cnt = 0
        for j in input():
            tmp.append(int(j))
            if int(j) == 2:
                start = [i, cnt]
            if int(j) == 3:
                end = [i, cnt]
            cnt += 1
        maze.append(tmp)




    print(maze)
