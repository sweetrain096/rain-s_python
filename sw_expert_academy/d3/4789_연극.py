import sys
sys.stdin = open("4789_input.txt")

for tc in range(int(input())):
    test = input()
    result = 0
    sum_people=0
    for i in range(len(test)):
        if int(test[i]) and sum_people < i:
            result += i - sum_people
            sum_people += i - sum_people

        sum_people += int(test[i])

    print(f"#{tc + 1} {result}")
