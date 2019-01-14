number = int(input())
result = [i-1 for i in range(number+1, 0, -1)]

print(" ".join(map(str, result)))