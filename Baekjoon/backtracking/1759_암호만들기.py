import sys
sys.stdin = open("1759_input.txt")

def dfs(index):
    result.append(data[index])
    visited[index] = 1
    if len(result) == l:
        check_con = 0
        check_vow = 0
        for check in result:
            if check in vowels:
                check_vow += 1
            else:
                check_con += 1

            if check_con >= 2 and check_vow >= 1:
                print('result', ''.join(result))


    for i in range(index + 1, c):
        # print(''.join(result))
        # print(visited)
        if len(result) < 4 and not visited[i]:
            dfs(i)
    result.pop()
    visited[index] = 0



l, c = map(int, input().split())
data = sorted(list(input().split()))
vowels = 'aeiou'

print(data)
for choice in range(c - l + 1):
    visited = [0] * c
    result = []
    dfs(choice)
