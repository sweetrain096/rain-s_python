import sys
sys.stdin = open("4866_input.txt")



def solution(brackets):
    stack = []
    check_list = ['(', ')', '{', '}']
    for bracket in brackets:

        if bracket in check_list:
            if bracket == check_list[0] or bracket == check_list[2]:
                stack.append(bracket)
            elif bracket == check_list[1]:
                if len(stack) == 0 :
                    return 0
                check = stack.pop()
                if not check == check_list[0]:
                    return 0
            elif bracket == check_list[3]:
                if len(stack) == 0 :
                    return 0
                check = stack.pop()
                if not check == check_list[2]:
                    return 0

    if stack:
        return 0
    else:
        return 1


for tc in range(int(input())):
    test = input()
    print(f"#{tc + 1} {solution(test)}")

