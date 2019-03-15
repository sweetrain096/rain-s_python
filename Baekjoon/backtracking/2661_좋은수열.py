import sys
sys.stdin = open("2661_input.txt")

def dfs(n, tmp):
    global result
    # print(1, tmp)
    if len(tmp) == n:
        now = int(''.join(map(str, tmp)))
        print(now)
        result = min(result, now)
    elif len(tmp) > n:
        return
    flag = True
    for i in data:
        if not tmp:
            tmp.append(i)
            print("1", tmp)
            dfs(n, tmp)
        elif tmp[-1] != i:

            print(tmp, tmp[-1], i)
            for i in range(2, len(tmp) // 2 + 1):
                print("hi", tmp[-1:-(i + 1)], tmp[-(i + 1):-(2 * i + 1)])
                if tmp[-1:-(i + 1)] == tmp[-(i + 1):-(2 * i + 1)]:
                    flag = False
                    break
    if flag:
        tmp.append(i)
        dfs(n, tmp)
    tmp.pop()


    return
data = [1, 2, 3]
n = int(input())
result = int('3' * n)
tmp = []
dfs(n, tmp)
