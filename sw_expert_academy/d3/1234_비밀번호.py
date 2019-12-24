import sys
sys.stdin = open("1234_input.txt")

for tc in range(10):
    tmp = input().split()
    n = int(tmp[0])
    numbers = [_ for _ in tmp[1]]
    new_len = n
    while True:
        check = -1
        cnt_len = 0
        for i in range(n):
            if numbers[i]:
                # 0번째 체크
                if check == -1:
                    check = i
                    continue
                if numbers[check] == numbers[i]:
                    numbers[check] = 0
                    numbers[i] = 0
                    check = -1
                    continue
                if numbers[check] != numbers[i]:
                    check = i
                    cnt_len += 1
        if cnt_len == new_len:
            break
        new_len = cnt_len
    result = ""
    for num in numbers:
        if num:
            result += num
    print(f"#{tc + 1} {result}")





