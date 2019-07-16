strings = '2+3*4/5'

Operator = ['+', '-', '*', '/']
stack = []
def isnumber(char):
    if char in Operator:
        stack.append(char)
    else:
        print(char, end="")

for string in strings:
    isnumber(string)

for push_stack in range(len(stack)):
    print(stack.pop(), end="")
