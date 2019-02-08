import sys
sys.stdin = open("6190_input.txt")

for tc in range(int(input())):
    n = int(input())
    numbers = list(map(int,input().split()))
    result = 0
    for number in range(n):
        for second_number in range(number + 1, n):
            mul = str(numbers[number] * numbers[second_number])
            if int(mul) <= result:
                continue
            if len(mul) == 1 :
                if result < int(mul):
                    result = int(mul)
            else:
                check = mul[0]
                for n_int in mul:
                    if int(check) <= int(n_int):
                        check = n_int
                    else:
                        mul = 0
                        break
                if result < int(mul):
                    result = int(mul)

    if not result:
        result = -1

    print(f"#{tc + 1} {result}")














# for tc in range(int(input())):
#     n = int(input())
#     numbers = list(map(int,input().split()))
#     result = 0
#     for number in range(n):
#         if number != 0:
#             mul = str(numbers[number] * numbers[number - 1])
#             if len(mul) == 1 :
#                 if result < int(mul):
#                     result = int(mul)
#             else:
#                 check = mul[0]
#                 for n_int in mul:
#                     if int(check) <= int(n_int):
#                         check = n_int
#                     else:
#                         mul = 0
#                         break
#                 if result < int(mul):
#                     result = int(mul)
