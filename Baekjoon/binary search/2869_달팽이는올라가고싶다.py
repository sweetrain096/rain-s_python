import sys
sys.stdin = open("2869_input.txt")


def is_up(day):
    sum_a = a * day
    # 일수가 너무 많이 남을 때
    if sum_a - v - b > a:
        return -1
    total = a * day - b * (day-1)
    # 성공
    if total == v or 0 < total - v < a:
        return 1
    # 너무 일수가 많이 남을 때
    elif total > v:
        return -1
    # 실패할 때
    return 0
    # for i in range(day):
    #     total += a
    #     if i == day-1 and total >= v:
    #         # 성공
    #         return 1
    #     elif total >= v and i < day-1:
    #         # 너무 일수가 많이 남을때
    #         return -1
    #     total -= b
    # 실패할 때
    # return 0

def binary_search(left, right, pick):
    global result
    if is_up(pick) == 1:
        result = pick
        return pick
    elif is_up(pick) == -1:
        binary_search(left, pick-1, (left + pick) // 2)
    elif is_up(pick) == 0:
        binary_search(pick + 1, right, (pick+right) // 2)


a, b, v = map(int, input().split())
result = 1
binary_search(1, 1000000000, (1+1000000000)//2)
print(result)
