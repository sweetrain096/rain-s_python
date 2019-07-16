data = [7, 4, 2, 0, 0, 6, 0, 7, 0]
result = 0
max_height = 0
for i in range(len(data)):
    max_height = len(data) - (i + 1)
    for j in range(i + 1, len(data)):
        if data[i] <= data[j]:
            max_height -=1
    if result <max_height:
        result = max_height
print(result)