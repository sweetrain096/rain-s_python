import sys
sys.stdin = open("Yellow_Cards_input.txt")

def min_cnt(a1, a2, k1, k2, n):
    cnt = 0
    if k1>k2:
        for i in range(len(a1)):
            if n-(a1[i]-1)>=0:
                n -= a1[i] - 1
                a1[i] = 1
            else:
                return cnt
        for i in range(len(a2)):
            if n-(a2[i]-1)>=0:
                n -= a2[i] - 1
                a2[i] = 1
            else:
                return cnt
    else:
        for i in range(len(a2)):
            if n-(a2[i]-1)>=0:
                n -= a2[i] - 1
                a2[i] = 1
            else:
                return cnt
        for i in range(len(a1)):
            if n-(a1[i]-1)>=0:
                n -= a1[i] - 1
                a1[i] = 1
            else:
                return cnt

    for i in a1 + a2:
        if n-i >= 0:
            n -= i
            cnt += 1
        else:
            return cnt
    return cnt

def max_cnt(a1, a2, k1, k2, n):
    cnt = 0
    if k1<k2:
        for i in range(len(a1)):
            if n-a1[i] >= 0:
                n -= a1[i]
                a1[i] = 0
                cnt += 1
            else:
                return cnt
        for i in range(len(a2)):
            if n - a2[i] >= 0:
                n -= a2[i]
                a2[i] = 0
                cnt += 1
            else:
                return cnt
    else:
        for i in range(len(a2)):
            if n - a2[i] >= 0:
                n -= a2[i]
                a2[i] = 0
                cnt += 1
            else:
                return cnt
        for i in range(len(a1)):
            if n - a1[i] >= 0:
                n -= a1[i]
                a1[i] = 0
                cnt += 1
            else:
                return cnt
    return cnt



a1 = int(input())
a2 = int(input())

k1 = int(input())
k2 = int(input())

n = int(input())

A1_list = [k1 for _ in range(a1)]
A2_list = [k2 for _ in range(a2)]


result_min = min_cnt(A1_list[:], A2_list[:], k1, k2, n)
result_max = max_cnt(A1_list[:], A2_list[:], k1, k2, n)
print(result_min, result_max)