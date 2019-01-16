numbers = input()
length = len(numbers)
check_number = ""
pre_numbers = ""
sum_numbers = ""

if length == 1:
    a = 0
    b = numbers[0]
    pre_numbers = numbers
    sum_numbers = str(a + int(b))
    numbers = "0"+numbers

else:
    a = numbers[0]
    b = numbers[1]
    pre_numbers = numbers
    sum_numbers = str(int(a) + int(b))
cnt = 1

while True :
    a = pre_numbers[-1]
    b = sum_numbers[-1]

    pre_numbers = sum_numbers
    check_number = a + b
    sum_numbers = str(int(a) + int(b))

    if check_number == numbers :
        print(cnt)
        break
    cnt += 1