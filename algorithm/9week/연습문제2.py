'''
16진수 문자로 이루어진 1차 배열이 주어질 때
앞에서부터 7bit씩 묶어 십진수로 변환하여 출력
input
0F97A3 = > 7, 101, 116, 3
01D06079861D79F99F
'''
# 16진수 계산하는 코드도 좋지만, mapping table을 만들어 바로 접근할 수 있게
# 하는 것이 가장 빠른 속도를 낼 수 있다.
arr = list(input())
data = []
for i in arr:
    if ord(i) >= 65:
        num = ord(i) - 55
    else:
        num = int(i)

    tmp = []
    for j in range(4):
        if num % 2:
            tmp.append(1)
            num = num // 2
        else:
            tmp.append(0)
            num = num // 2
    data += tmp[::-1]

total = len(data)
n = 0
for i in range(total):
    n = n * 2 + data[i]
    if i % 7 == 6:
        print(n, end=" ")
        n = 0
if n:
    print(n)


print(data)