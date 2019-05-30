'''
3 개 중에 2개를 중복해서 고르는 순열
'''

def permutation(n, r):
    if not r:
        print(t[::-1][1:])
    else:
        for i in range(n - 1, -1, -1):
            # 현재 위치(가장 끝? 선택한 것?)와 자기자신을 포함한
            # 앞에 위치한 숫자와 교환
            a[i], a[n - 1] = a[n - 1], a[i]
            t[r - 1] = a[n - 1]
            permutation(n, r - 1)
            a[i], a[n - 1] = a[n - 1], a[i]


a = [1, 2, 3]
t = [0] * 3
permutation(3, 2)