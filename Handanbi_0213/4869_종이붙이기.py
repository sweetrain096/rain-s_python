import sys
sys.stdin = open("4869_input.txt")



def solution(n):
    global cnt
    n = n // 10

    result = [1]


    for i in range(1, n + 1):

        if not cnt % 2:
            result.append(result[i - 1] * 2 + 1)
        else:
            result.append(result[i - 1] * 2 - 1)
        cnt += 1
    return result[n - 1]


for tc in range(int(input())):
    cnt = 0

    n = int(input())
    result = solution(n)


    print(f"#{tc + 1} {result}")

