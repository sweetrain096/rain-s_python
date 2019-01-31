'''
영어 이름 출력하기
영어 이름은 가운데 이름을 가지고 있는 경우가 있습니다.

가운데 이름은 축약해서 나타내는 함수를 작성해보세요.

예시 입력)
Alice Betty Catherine Davis
예시 출력)
Alice B. C. Davis
'''

name = input().split()
result = []
for length in range(len(name)):
    if len(name) <= 2:
        result.append(name[length])

    else:
        if length == 0 or length == len(name)-1:
            result.append(name[length])
        else:
            result.append(f"{name[length][0]}"+".")

print(f"{' '.join(result)}")