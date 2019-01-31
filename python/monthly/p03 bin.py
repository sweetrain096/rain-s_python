def my_bin(x):
    result = ""

    while x > 0:
        result += str(x % 2)
        x = x // 2
    result = "0b"+result[::-1]

    return result

print(my_bin(4096), my_bin(5))