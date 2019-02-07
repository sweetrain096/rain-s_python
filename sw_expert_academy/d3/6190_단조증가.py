import sys
sys.stdin = open("6190_input.txt")

for tc in range(int(input())):
    n = int(input())
    numbers = list(map(int,input().split()))
    check = 0
    for number in range(n):
        if number != 0:
            mul = str(numbers[number] * numbers[number - 1])


        # if len(numbers[number]) == 1 and number != 0 :
        #     if mul < int(numbers[number]) * int(numbers[number - 1]):
        #         mul = int(numbers[number]) * int(numbers[number - 1])
        # else:
        #     check = numbers[number][0]
        #     for n_int in numbers[number]:
        #         if check > n_int:
        #             numbers[number] = 0
        #     if mul < int(numbers[number]) * int(numbers[number - 1]):
        #         mul = int(numbers[number]) * int(numbers[number - 1])
        #
        # if mul == 0:
        #     mul = -1


    print(f"#{tc + 1} {numbers} {mul}")