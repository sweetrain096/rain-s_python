T = int(input())
for i in range(T) :
    numbers = list(map(int, input().split(" ")))
    result = numbers[0]
    for number in numbers :
        if number > result :
            result = number

    print(f"#{i+1} {result}")