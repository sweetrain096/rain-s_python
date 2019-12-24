import sys
sys.stdin = open("1218_input.txt")

for tc in range(10):
    n = int(input())
    data = input()
    check = dict()
    result = 1

    for i in data:
        if i in ['(', '<', '{', '[']:
            if not check.get(i):
                check[i] = 1
            else:
                check[i] += 1
        else:
            if i == ')':
                if check.get('('):
                    check['('] -= 1
                else:
                    result = 0
            elif i == '>':
                if check.get('<'):
                    check['<'] -= 1
                else:
                    result = 0
            elif i == '}':
                if check.get('{'):
                    check['{'] -= 1
                else:
                    result = 0
            else:
                if check.get('['):
                    check['['] -= 1
                else:
                    result = 0
        if not result:
            break
    print(f"#{tc + 1} {result}")