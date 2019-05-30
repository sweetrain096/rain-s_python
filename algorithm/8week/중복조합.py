'''
중복되게 4H3
'''

def combination(n, r, q):
    # 뽑을 수 있는 값이 없을 때 print
    if not r:
        print(T)
    # 모두 다 선택하여 더 이상 뽑을 수 있는 후보가 없을 때 return 
    elif not n:
        return
    else:
        T[r - 1] = A[n - 1]
        combination(n, r - 1, q)
        combination(n - 1, r, q)


A = [1, 2, 3, 4]
T = [0] * 3
combination(4, 3, 3)