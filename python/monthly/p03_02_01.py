def tax(won):
    result = 0
    if won > 4600:
        check = won - 4600
        won -= check
        result += check * 0.35
    if won > 1200:
        check = won - 1200
        won -= check
        result += check * 0.15
    if won <= 1200:
        result += won * 0.06
    return result


print(tax(1200))
print(tax(4600))
print(tax(5000))