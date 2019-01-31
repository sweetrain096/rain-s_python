def collatz(number):
    result = -1
    for cnt in range(500):
        if not number % 2:
            number = number / 2
        else:
            number = number * 3 + 1

        if number == 1 :
            result = cnt + 1
            break
    return result


print(collatz(6))
print(collatz(16))
print(collatz(27))
print(collatz(626331))