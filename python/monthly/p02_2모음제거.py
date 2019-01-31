'''
다음 문장의 모음을 제거하여 출력하세요.

예시 입력)
"Life is too short, you need python"
예시 출력)
Lf s t shrt, y nd pythn
'''

string = input()
check_list = "aeiou"

for char in string :
    if char not in check_list:
        print(char, end="")
