def process_solution(a, k):
    sum_data = 0
    for i in range(1, k + 1):
        if a[i]:
            sum_data += data[i]
            # print(data[i], end=" ")
    if sum_data == 10:
        for i in range(1, k + 1):
            if a[i]:
                print(data[i], end=" ")

        print()

def make_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2



# a = 원본 list    k = 0(초기값 및 input과 같아지기 위해 커지는 값)   input : depth.
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k)
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input)








# 임의의 값(공간)을 미리 확보
MAXCANDIDATES = 100
NMAX = 100


# 부분집합을 만들 원본 데이터
data = [i for i in range(11)]
print(data)
a = [0] * NMAX
backtrack(a, 0, 10)