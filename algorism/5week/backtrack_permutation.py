def process_solution(a, k):
    for i in range(1, k + 1):

        print(data[a[i]], end=" ")
    print()

def make_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        # a[i]가 2면, (== 이미 2를 포함한 순열이면)
        in_perm[a[i]] = True
        # in_perm[2] index(2)를 포함했다고 True로 처리.(visited와 유사하다.)

    ncands = 0
    for i in range(1, input + 1):
        if in_perm[i] == False:
            c[ncands] = i
            ncands += 1
    return ncands

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

MAXCANDIDATES = 100
NMAX = 100
data = [0, 1, 2, 3]
a = [0] * NMAX
backtrack(a, 0, 3)