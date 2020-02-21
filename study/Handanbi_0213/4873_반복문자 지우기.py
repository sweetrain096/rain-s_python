import sys
sys.stdin = open("4873_input.txt")

for tc in range(int(input())):
    stack = []
    for string in input():
        if not len(stack) or stack[-1] != string:
            stack.append(string)
        else:
            stack.pop()



    print(f"#{tc + 1} {len(stack)}")