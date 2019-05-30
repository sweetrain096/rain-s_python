def Bit(i):
    result = ""
    for j in range(7, -1, -1):
        result += "1" if i & (1 << j) else "0"
    return result


for i in range(-5, 6):
    result = Bit(i)
    print("{} = {}".format(i, result))
    # print("%3d = %d" %i %result)