import sys
sys.stdin = open("7508_input.txt")


def find_able(i):
    if ableIdx[i] == -1:
        return -1
    return idx[ableIdx[i]]


for tc in range(int(input())):
    time = 0
    n = int(input())
    able = sorted(list(map(int, input().split())))
    ableIdx = [0 for _ in range(n)]
    m = int(input())
    weights = list(map(int, input().split()))
    cnts = dict()
    for i in weights:
        if cnts.get(i):
            cnts[i] += 1
        else:
            cnts[i] = 1
    idx = sorted(list(set(weights)))

    if able[-1] < idx[-1]:
        print(f"#{tc + 1} -1")
        continue

    ableIdxCnt = n - 1
    for i in range(len(idx)-1, -1, -1):
        while able[ableIdxCnt] >= idx[i]:
            ableIdx[ableIdxCnt] = i
            ableIdxCnt -= 1
            if ableIdxCnt == -1:
                break
        if ableIdxCnt == -1:
            break
    # print(idx)
    # print(ableIdx)


    while cnts:
        time += 1
        for i in range(n-1, -1, -1):
            now = find_able(i)
            if now == -1:
                continue
            # print(i, now, cnts, ableIdx, idx)
            cnts[now] -= 1
            if cnts[now] == 0:
                cnts.pop(now)
                idx[ableIdx[i]] = -1
                # idx.pop(idx.index(now))
                new = -1
                for j in range(ableIdx[i] - 1, -1, -1):
                    if idx[j] != -1:
                        new = j
                        break
                # print("new", new)
                for j in range(i - 1, -1, -1):
                    if ableIdx[i] == ableIdx[j]:
                        ableIdx[j] = new
                    else:
                        break
                for j in range(i + 1, len(ableIdx)):
                    if ableIdx[i] == ableIdx[j]:
                        ableIdx[j] = new
                    else:
                        break
                ableIdx[i] = new
        # print(i, now, cnts, ableIdx, idx)
    print(f"#{tc + 1} {time}")