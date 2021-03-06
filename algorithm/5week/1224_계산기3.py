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

    print(''.join(map(str, postfix_notation)))

    while len(postfix_notation) != 0:
        # print(stack, type(postfix_notation[0]))
        if type(postfix_notation[0]) == int:
            stack.append(postfix_notation.pop(0))
        elif type(postfix_notation[0]) == str:
            operator = postfix_notation.pop(0)
            num2 = stack.pop()
            num1 = stack.pop()
            if operator == "+":
                stack.append(num1 + num2)
            else:
                stack.append(num1 * num2)
    if not postfix_notation:
        result = stack.pop()




    print("#{} {}".format(tc + 1, result))