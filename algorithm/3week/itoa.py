def itoa(x):
    arr = []

    while True:
        arr.append(chr(x % 10 + ord('0')))
        x = x // 10
        if x == 0 :
            break

    arr = arr[::-1]
    return ''.join(arr)

x = 123
print(x, type(x))
str1 = itoa(x)
print(str1, type(str1))