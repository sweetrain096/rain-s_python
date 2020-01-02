import sys
sys.stdin = open("11279_new_input.txt")

import heapq

heap = []
for n in range(int(input())):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(heap, -1 * x)
    else:
        try:
            print(-1*heapq.heappop(heap))
        except:
            print(0)