import sys
sys.stdin = open("1224_input.txt")

priority_list = {'*' : 2, '/' : 2, '+' : 1, '-' : 1, '(' : 0}

for tc in range(10):
    length = int(input())
    infix_notation = input()
    stack = []
    postfix_notation = []
    for token in infix_notation:

        if token == '(':
            stack.append(token)
        elif not priority_list.get(token):
            postfix_notation.append(int(token))
        elif token == ')':
            while stack[-1] == '(':
                postfix_notation.append(stack.pop())

        else:
            cnt = -1
            # print(priority_list.get(stack[cnt]), priority_list.get(token) )
            while priority_list.get(stack[cnt]) < priority_list.get(token):
                stack.append(token)
            postfix_notation.append(stack.pop())

        print(stack, postfix_notation)



    print(f"#{tc + 1} {postfix_notation}")