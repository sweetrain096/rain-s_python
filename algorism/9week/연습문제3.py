'''
16진수 문자로 이루어진 1차 배열이 주어질 때,
암호비트 패턴을 찾아 차례대로 출력
암호는 연속되어있다.
ex) 0DEC인 경우, 0, 2가 출력
ex) 0269FAC9A0

+ plus
암호의 패턴이 맨 뒤가 1로 끝나는 것으로 같기 때문에,
맨 뒤에서부터 1이 있는 부분을 찾아나가는 방식으로
검증하는것이 쉽다.
'''

asc = [[0,0,0,0],
        [0,0,0,1],
        [0,0,1,0],
        [0,0,1,1],
        [0,1,0,0],
        [0,1,0,1],
        [0,1,1,0],
        [0,1,1,1],
        [1,0,0,0],
        [1,0,0,1],
        [1,0,1,0],
        [1,0,1,1],
        [1,1,0,0],
        [1,1,0,1],
        [1,1,1,0],
        [1,1,1,1]]

pattern = [[0, 0, 1, 1, 0, 1],
           [0, 1, 0, 0, 1, 1],
           [1, 1, 1, 0, 1, 1],
           [1, 1, 0, 0, 0, 1],
           [1, 0, 0, 0, 1, 1],
           [1, 1, 0, 1, 1, 1],
           [0, 0, 1, 0, 1, 1],
           [1, 1, 1, 1, 0, 1],
           [0, 1, 1, 0, 0, 1],
           [1, 0, 1, 1, 1, 1]]

input_data = list(input())
data = []
for i in input_data:
    if ord(i) >= 65:
        data += asc[ord(i) - 55]
    else:
        data += asc[int(i)]
print(data)

result = []
start = 0
for i in range(len(data)):
    if start > len(data):
        break
    for mat in range(10):
        if not start:
            print(pattern[mat], data[i : i + 6])
            if pattern[mat] == data[i : i + 6]:
                result.append(mat)
                start = i + 6
        else:
            if pattern[mat] == data[start : start + 6]:
                result.append(mat)
                start = start + 6

print(result)