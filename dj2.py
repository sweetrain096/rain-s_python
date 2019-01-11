number = int(input())
result = [i * 2 for i in range(number + 1)]
print(result)
print(" ".join(map(int, result)))