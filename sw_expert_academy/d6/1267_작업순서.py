import sys
sys.stdin = open("1267_input.txt")

def find():
    stack = []
    for i in range(1, v + 1):
        if not degree[i]:
            stack.append(i)
    result = []
    while stack:
        t = stack.pop()
        result.append(t)
        for i in range(1, v + 1):
            if graph[t][i]:
                degree[i] -= 1
                if not degree[i]:
                    stack.append(i)
    return result



for tc in range(10):
    v, e = map(int, input().split())
    data = list(map(int, input().split()))
    graph = [[0 for _ in range(v + 1)] for _ in range(v + 1)]

    degree = [0 for _ in range(v + 1)]

    for i in range(e):
        num1, num2 = data[i * 2], data[i * 2 + 1]
        graph[num1][num2] = 1

        degree[data[i * 2 + 1]] += 1


    print("#{} {}".format(tc + 1, ' '.join(map(str, find()))))


