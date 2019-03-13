import sys
sys.stdin = open("2193_input.txt")

def pinary_num(number):
    numbers = [0, 1]
    for i in range(2, number + 1):
        numbers.append(numbers[i - 2] + numbers[i - 1])
    return numbers[number]

n = int(input())
print(pinary_num(n))
