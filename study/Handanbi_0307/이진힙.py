import sys
sys.stdin = open("이진힙.txt")

for tc in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    heap = [0 for i in range(n + 1)]
    for i in range(n):
        heap[i + 1] = data[i]
        now = i + 1
        while heap[now // 2] > heap[now]:
            heap[now // 2], heap[now] = heap[now], heap[now // 2]
            now = now // 2

    check = n
    plus = 0
    while check:
        plus += heap[check // 2]
        check = check // 2

    print("#{} {}".format(tc + 1, plus))