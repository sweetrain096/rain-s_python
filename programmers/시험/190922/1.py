import sys
sys.stdin = open("1_input.txt")

M, C = map(int, input().strip().split(' '))
# QC = [[0] for _ in range(C)]
SC = [0 for _ in range(C)]

for i in range(M):
    m = int(input())
    min_C = min(SC)
    min_index = SC.index(min_C)
    # QC[min_index].append(m)
    SC[min_index] += m

    # print(QC)
# print(SC)
print(max(SC))