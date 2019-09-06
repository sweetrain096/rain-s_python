relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

import itertools



def solution(relation):
    row = len(relation)
    col = len(relation[0])
    col_nums = [i for i in range(1, col + 1)]
    candidates = []

    for i in range(1, col + 1):
        els = [list(x) for x in itertools.combinations(col_nums, i)]
        candidates.extend(els)
    print(candidates)

    result = []

    for check_list in candidates:
        print(check_list)
        test_data = []
        for index in check_list:
            print(relation[:])
            test_data += relation[:][index]
        print(test_data)



    answer = 0
    visited = {}







    for c in range(col):
        check = {}
        is_true = True
        for r in range(row):
            print(relation[r][c])
            if check.get(relation[r][c]):
                is_true = False
                break
            check[relation[r][c]] = 1
        if is_true:
            visited[c] = 1
    print(visited)
    return answer










solution(relation)