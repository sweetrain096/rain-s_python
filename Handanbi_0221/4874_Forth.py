import sys
sys.stdin = open("4874_input.txt")

operators = ['+', '-', '*', '/']

def find_operation():
    for operation in operation_list:
        if operation == '.':
            result = int(stack.pop())
            return result
        elif operation in operators:
            num2 = stack.pop()
            num1 = stack.pop()

            if operation == '+':
                stack.append(num1 + num2)
            elif operation == '-':
                stack.append(num1 - num2)
            elif operation == '*':
                stack.append(num1 * num2)
            elif operation == '/':
                stack.append(num1 / num2)
        else:
            stack.append(int(operation))


for tc in range(int(input())):
    stack = []
    operation_list = list(input().split())
    operator_cnt, num_cnt = 0, 0
    for operation in operation_list:
        if operation == '.':
            pass
        elif operation in operators:
            operator_cnt += 1
        else:
            num_cnt += 1
    if num_cnt != operator_cnt + 1:
        result = 'error'
    else:
        result = find_operation()


    print(f"#{tc + 1} {result}")