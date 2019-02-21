import sys
sys.stdin = open("4880_input.txt")

def game(person1, person2):
    if person1 == person2:
        return person1
    elif person1 == 1 and person2 == 3:
        return person1
    elif person1 == 3 and person2 == 1:
        return person2
    elif person1 > person2:
        return person1
    elif person2 > person1:
        return person2


def divide(i, j):
    mid = (i + j) // 2

    if len(people_list[i : j + 1]) == 2:
        a, b = people_list[i][0], people_list[j][0]
        winner = game(a, b)
        # print('winner', winner)
        if a == winner:
            # print(people_list[i])
            return people_list[i]
        else:
            # print(people_list[j])
            return people_list[j]

    elif len(people_list[i : j + 1]) == 1:
        return people_list[i]

    # print('list', people_list[i: j + 1])
    l_win = divide(i, mid)
    r_win = divide(mid + 1, j)


    # print('hi',l_win, r_win)
    a, b = l_win[0], r_win[0]
    winner = game(a, b)
    if winner == a:
        return l_win
    else:
        return r_win

    # return game(l_win, r_win)





for tc in range(int(input())):
    n = int(input())
    people_list = list(map(int, input().split()))
    people_list.insert(0, 0)
    # print(people_list)
    for i in range(n + 1):
        people_list[i] = [people_list[i], i]
    # print(people_list)




    result = divide(1, n)


    print(f"#{tc + 1} {result[1]}")
