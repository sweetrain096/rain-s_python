'''
0과 1로 이루어진 1차 배열에서 7개 byte를 묶어 10진수로 출력

input :
0000000111100000011000000111100110000110000111100111100111111001100111
'''

data = list(input())
print(data)

cnt = 0
result = ""
while True:
    cnt += 1
    result += data[cnt - 1]

    if not cnt % 7:
        print(int('0b' + result, 2), end=" ")
        result = ""

    if cnt == len(data):
        if result:
            print(int('0b' + result, 2))
        break
print()
for i in range(10):
    n = 0
    for j in range(i * 7, i * 7 + 7):
        n = n * 2 + int(data[j])
    print(n, end=" ")