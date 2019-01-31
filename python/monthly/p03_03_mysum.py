def my_sum(num1, num2):
    diff = len(num1) - len(num2)
    num1 = -diff * '0' + num1
    num2 = diff * '0' + num2
    result = 0
    plus = 0

    for cnt in range(len(num1)):

        sum_check = plus + int(num1[-(cnt + 1)]) + int(num2[-(cnt + 1)])
        plus = 0

        if sum_check >= 10:
            plus += 1
            sum_check = sum_check % 10
        if not cnt:
            result += sum_check

        result += sum_check * 10 * cnt

    return result


print(my_sum('3', '5'))
print(my_sum('123', '77'))
print(my_sum('1', '9999'))