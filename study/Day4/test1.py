# '''
# 문제 1.
# 문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.
# '''

# str = input('문자를 입력하세요: ')
# # 아래에 코드를 작성해 주세요.
# print(str[0], str[-1])

# '''
# 문제 2.
# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
# '''

# n = int(input('숫자를 입력하세요: '))
# # 아래에 코드를 작성해 주세요.
# for i in range(1, n+1) :
#     print(i)

# '''
# 문제 3.
# 숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
# '''

# number = int(input('숫자를 입력하세요: '))
# # 아래에 코드를 작성해 주세요.
# # 1이면 ture 0이면 false
# if number%2 :
#     #number%2 가 1이므로 true일때 조건문 실행. 결국 '==1' 부분을 안써도 가능
#     print("홀수입니다.")
# else :
#     print("짝수입니다.")


# '''
# 문제 4.
# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
# 국어는 90점 이상,
# 영어는 80점 초과,
# 수학은 85점 초과, 
# 과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면 불합격)
# 다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 
# '''

# a = int(input('국어: '))
# b = int(input('영어: '))
# c = int(input('수학: '))
# d = int(input('과학: '))
# # 아래에 코드를 작성해 주세요.
# if a>=90 and b>80 and c>85 and d>=80 :
#     print("True")
# else :
#     print("False")

# # 위의 조건문을 print(a>=90 and b>80 and c>85 and d>=80) 한줄로 바꿔도 True 또는 False 출력 가능


'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''

prices = input('물품 가격을 입력하세요: ')
# 아래에 코드를 작성해 주세요.
prices = prices.split(';')
for i in range(len(prices)) :
    prices[i] = int(prices[i])
print(prices)
# prices = list(map(int, prices))


prices.sort(reverse=True)
print(prices)
