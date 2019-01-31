def lonely(lists):
    result = []
    for cnt in range(len(lists)):
        if cnt == 0:
            result.append(lists[cnt])
        else :
            if not result[-1] == lists[cnt]:
                result.append(lists[cnt])

    return result

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4,4,4,3,3]))