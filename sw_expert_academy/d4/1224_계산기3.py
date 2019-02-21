import sys
sys.stdin = open("1224_input.txt")

priority_list = {'*' : 2, '+' : 1, '(' : 0}

for tc in range(10):
    length = int(input())
    infix_notation = input()
    stack = []
    postfix_notation = []
    for token in infix_notation:

        if token == '(':
            stack.append(token)
        elif token == ')':
            while True:
                top = stack.pop()
                if top != '(':
                    postfix_notation.append(top)
                else:
                    break
                # print(stack, postfix_notation)
        elif not priority_list.get(token):
            postfix_notation.append(int(token))


        else:
            # print(priority_list.get(stack[cnt]), priority_list.get(token) )
            if not stack:
                stack.append(token)
            else:
                # print(stack, postfix_notation)
                while len(stack) != 0 and priority_list.get(stack[-1]) >= priority_list.get(token):
                    # print(priority_list.get(stack[-1]), priority_list.get(token))
                    # print(stack, postfix_notation)
                    postfix_notation.append(stack.pop())
                stack.append(token)


        # print(stack, postfix_notation)


    if stack:
        while len(stack) != 0:
            postfix_notation.append(stack.pop())

    print(f"#{tc + 1} {postfix_notation}")