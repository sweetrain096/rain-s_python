import sys
sys.stdin = open("3143_input.txt")

for tc in range(int(input())):
    A, B = input().split()
    i = 0
    cnt = 0
    while i <= len(A) - len(B):
        # print(i, cnt)
        flag = 1
        for j in range(len(B)):
            if A[i + j] != B[j]:
                flag = 0
                break
        if flag:
            cnt += 1
            i += len(B)
            # print("I", i)
            continue

        i += 1
        cnt += 1
    cnt += len(A) - i
    print(f"#{tc + 1} {cnt}")