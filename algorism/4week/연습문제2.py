def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        print("stack is empty!")
        return
    else:
        return stack.pop()


def solution(brackets):

    for bracket in brackets:
        if bracket == '(':
            push(bracket)
        elif bracket == ')':
            check = pop()
            if not check == '(':
                print("False")
                return False
    if stack:
        return False
    else:
        return True


stack = []



print(solution('()()((()))'))
print(solution('((()((((()()((()())((())))))'))
print(solution(')('))