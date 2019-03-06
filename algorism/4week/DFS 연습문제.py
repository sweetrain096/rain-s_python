import sys
sys.stdin = open("dfs_input.txt")

# 반복문
def dfs(n):
    stack = []
    result = []
    stack.append(n)
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = 1
            result.append(node)
            for w in range(v + 1):
                if graph[node][w] and not visited[w]:
                    stack.append(w)

    return result
result = []
# 재귀
def dfs2(n):

    visited[n] = 1
    result.append(n)
    for w in range(v + 1):
        if graph[n][w] and not visited[w]:
            return dfs2(w)
# 재귀
def dfs3(n):
    global graph, visited, v
    visited[n] = 1
    print(n, end=" ")

    for w in range(1, v+1):
        if graph[n][w] == 1 and visited[w] == 0:
            dfs(w)





# 정점, 간선
v, e = map(int, input().split())
temp = list(map(int, input().split()))

# graph = [[0] * (v + 1)] * (v + 1)     # 이 방법은 값이 하나가 바뀌면 모두 바뀐다.
graph = [[0 for i in range(v + 1)] for j in range(v + 1)]
visited = [0 for i in range(v + 1)]




for i in range(len(temp) // 2):

    w1, w2 = temp[i * 2 : (i + 1) * 2]
    # print(w1, w2)
    graph[w1][w2] = 1
    graph[w2][w1] = 1

for g in range(1, v + 1):
    print(graph[g][1:])



# result = dfs(1)
# print(result)

dfs2(1)
print(result)


# dfs3(1)
# print(result)