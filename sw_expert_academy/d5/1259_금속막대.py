import sys
sys.stdin = open("1259_input.txt")

def find_start_end():
    start = 0
    end = 0
    for key in check.keys():
        if start or end:
            if start:
                end = key
                return start, end
            if end:
                start = key
                return start, end

        for i in arr:
            if i[0] == key:
                start = key
                break
        if not start:
            end = key

for tc in range(int(input())):
    n = int(input())
    temp = list(map(int, input().split()))
    arr = []
    check = dict()
    numbers = dict()
    result = []
    for i in range(n):
        if check.get(temp[2 * i]):
            check.pop(temp[2 * i])
        else:
            check[temp[2 * i]] = 1
        if check.get(temp[2 * i + 1]):
            check.pop(temp[2 * i + 1])
        else:
            check[temp[2 * i + 1]] = 1
        new = (temp[2 * i], temp[2 * i + 1])
        numbers[temp[2 * i]] = new
        arr.append(new)
    start, end = find_start_end()
    now = start
    for i in range(n):
        result.append(numbers[now][0])
        result.append(numbers[now][1])
        now = numbers[now][1]
    print(f"#{tc + 1} {' '.join(map(str, result))}")