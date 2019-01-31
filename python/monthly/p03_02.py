def all(x):
    for in_x in x:
        if not in_x:
            return False
    return True

def any(x):
    for in_x in x:
        if in_x:
            return True
    return False

print(all([1, 2, 5, '6']))
print(all([[], 2, 5, [[]], '6']))
print(all([2, 5, [[]], '6']))
print(all([]))

print(any([1, 2, 5, '6']))
print(any([[], 2, 5, [[]], '6']))
print(any([2, 5, [[]], '6']))
print(any([{}, 2, 5, [[]], '6']))
print(any([]))
