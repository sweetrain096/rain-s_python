'''
중복되지 않게 4C3
'''

def combination(n, r):
    # 뽑을 수 있는 값이 없을 때 print == 조합이 존재
    if not r:
        return 1
    # 3 개 중에 4개를 뽑는 일어날 수 없는 상황일 때 return == 조합이 이루어질 수 없음
    elif n < r:
        return 0
    else:
        return combination(n - 1, r - 1) + combination(n - 1, r)


print(combination(5, 2))