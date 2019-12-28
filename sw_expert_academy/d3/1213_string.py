import sys
sys.stdin = open("1213_input.txt", encoding="UTF-8")

for tc in range(10):
    tn = int(input())
    find = input()
    len_str = len(find)
    target = input()
    cnt = 0
    for i in range(len(target)-len_str + 1):
        if target[i:i+len_str] == find:
            cnt += 1

    print(f"#{tn} {cnt}")