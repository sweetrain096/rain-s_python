def process_solution(a, k, sum_data):
    if sum_data != 10:
        return
    for i in range(1, k + 1):
        if a[i]:
            print(data[i], end=" ")
    print()

def make_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input, sum_data):
    if sum_data > 10:
        return
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k, sum_data)
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            # 가지치기. a[k]가 1일 때 data[k]의 값을 확인하여 더한다.
            if a[k]:
                backtrack(a, k, input, sum_data + data[k])
            else:
                backtrack(a, k, input, sum_data)



# 임의의 값(공간)을 미리 확보


MAXCANDIDATES = 100
NMAX = 100


# 부분집합을 만들 원본 데이터
data = [i for i in range(11)]
print(data)
a = [0] * NMAX
backtrack(a, 0, 10, 0)