def positive_sum(lists):
    result = 0
    for num in lists:
        if num > 0:
            result += num

    return result

print(positive_sum([1,-4,7,12]))
print(positive_sum([-1, -2, -3, -4]))