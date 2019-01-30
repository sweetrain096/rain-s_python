def revers(string):
    s_list = list(string)
    for cnt in range(int(len(string) / 2)):
        s_list[cnt], s_list[-(cnt + 1)] = s_list[-(cnt + 1)], s_list[cnt]

    return ''.join(s_list)

s = "Reverse this strings"
result = revers(s)







print(result)
