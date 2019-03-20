data = input()
check_list = []
cnt = 0

for i in data:
    if ord(i) >= 65 and ord(i) <= 90:
        check_list.append(i)
    elif ord(i) >= 97 and ord(i) <= 122:
        check_list[-1] += i
    else:
        cnt +=1

if cnt == len(check_list):
    for i in range(1, cnt + 1):
        if data[-i] != '1':
            check_list[-i] += data[-i]
    print(''.join(check_list))

else:
    print('error')
