import sys
sys.stdin = open("5432_input.txt")

for tc in range(int(input())):
    data = input()
    l = 0
    cnt = 0
    i = 0
    while i < len(data):
        if data[i] == '(':
            if data[i+1] == ')':
                cnt += l
                i += 2
                continue
            else:
                l += 1
        else:
            cnt += 1
            l -= 1
        i += 1
    print(f"#{tc + 1} {cnt}")
