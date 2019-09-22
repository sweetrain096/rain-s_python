'''
중복되지 않게 4C3
'''

def combination(n, r):
    # 뽑을 수 있는 값이 없을 때 print
    if not r:
        print(T)
    # 3 개 중에 4개를 뽑는 일어날 수 없는 상황일 때 return
    elif n < r:
        return
    else:
        T[r - 1] = A[n - 1]
        combination(n - 1, r - 1)
        combination(n - 1, r)


A = [1, 2, 3, 4]
T = [0] * 3
combination(4, 3)