relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

import itertools

def is_visited(visited, candidate):
    print("is_visited", visited, candidate)

    if visited:
        for visit_check in visited:
            print(visit_check)
            if len(set(visit_check + candidate)) == len(visit_check):
                return True
    return False

def solution(relation):
    data = [[0 for _ in range(len(relation))] for _ in range(len(relation[0]))]
    for r in range(len(relation)):
        for c in range(len(relation[0])):
            data[c][r] = relation[r][c]
    print(data)

    r, c = len(data), len(data[0])

    index_num = [i for i in range(r)]
    candidates = []

    for i in range(1, r + 1):
        candidates.extend([list(x) for x in itertools.combinations(index_num, i)])
    print(candidates)

    visited = []
    for candidate in candidates:
        print(is_visited(visited, candidate))
        # if is_visited(visited, candidate):
        #     continue

        test_data = [[] for _ in range(c)]
        for index in candidate:
            for in_index in range(c):
                test_data[in_index].append(data[index][in_index])
        for j in range(len(test_data)):
            test_data[j] = '/'.join(test_data[j])
        # print(test_data)
        # print(set(test_data))
        if c == len(set(test_data)):
            visited.append(candidate)
        print(visited)

        print(len(visited))



solution(relation)