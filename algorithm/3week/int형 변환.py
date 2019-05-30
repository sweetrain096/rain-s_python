def atoi(string):
    val = 0
    i = 0

    while (i < len(string)):
        c = string[i]
        if c >= '0' and c <= '9':
        # if ord(c) >= ord('0') and ord(c) <= ord('0') 이렇게 보면 좀 더 명확.
            digit = ord(c) - ord('0')
        else:
            break
        val = (val * 10) + digit
        i += 1
    return val



a = "123"
print(a, type(a))
b = atoi(a)
print(b, type(b))
c = int(a)
print(c, type(c))

