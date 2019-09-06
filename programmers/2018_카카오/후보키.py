relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]



def solution(relation):
    row = len(relation)
    col = len(relation[0])
    answer = 0

    for c in range(col):
        for r in range(row):
            print(relation[r][c])
    return answer


solution(relation)