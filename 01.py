char = input().split(" ")
total = len(char)
char_cnt = []
for i in range(total) :
    if char[i] :
        char_cnt.append(char[i])

print(len(char_cnt))