import sys
sys.stdin = open("2869_input.txt")


def is_up(day):
    total = 0
    for i in range(day):
        total += a
        if i == day-1 and total >= v:
            # 성공
            return 1
        elif total >= v and i < day-1:
            # 너무 일수가 많이 남을때
            return -1
        total -= b
    # 실패할 때
    return 0

def binary_search(left, right, pick):
    print(is_up(pick))
    if is_up(pick) == 1:
        print(pick)
        return pick
    elif is_up(pick) == -1:
        binary_search(left, pick-1, (left + pick) // 2)
    elif is_up(pick) == 0:
        binary_search(pick + 1, right, (pick+right) // 2)


a, b, v = map(int, input().split())
print(binary_search(1, 1000000000, (1+1000000000)//2))
