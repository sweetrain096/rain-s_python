import sys
sys.stdin = open("3752_input.txt")


for tc in range(int(input())):
    n = int(input())
    table = list(map(int, input().split()))
    result = [0]
    num_list = dict()
    num_list[0] = 1

    for plus in table:
        for num in range(len(result)):
            new = result[num] + plus
            if not num_list.get(new):
                result.append(new)
                num_list[new] = 1


    print(f"#{tc + 1} {len(list(set(result)))}")


