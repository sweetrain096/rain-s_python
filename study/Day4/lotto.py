import requests
import random
# 1. https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837 요청 보내기
url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
response = requests.get(url)


# 2. 응답 된 결과를 json으로 바꿔서 dictionary 처럼 활용한다.
lotto_json = response.json()
num = "drwtNo"
lotto_numbers = []
lotto_numbers.sort()
for i in range(6) :
    lotto_numbers.append(lotto_json[f"{num}{i+1}"])
lotto_numbers.append(lotto_json["bnusNo"])
#print(lotto_numbers)

# # 3. 랜덤으로 로또 번호 하나를 추출한다.
# # random_numbers = [2, 25, 28, 30, 33, 45]
# # print(random_numbers)
# random_numbers = random.sample(range(1,46), 6)
# random_numbers.sort()
# print(random_numbers)


# # 4. 몇 등인지 알아본다.
# # 1등 : 6개, 2등 : 5개+보너스, 3등 : 5개, 4등 : 4개, 5등 : 3개
# cnt = 0
# i = 0
# for n in random_numbers :
#     if n==lotto_numbers[i] :
#         cnt +=1
        
#     i +=1
    
#     if i==6 :
#         break
# print("cnt",cnt)




# win = "당첨되지 못했습니다."
# if random_numbers==lotto_numbers[:6] :
#     win = "1등"
# if cnt==3 :
#     win = "5등"
# elif cnt==4 :
#     win = "4등"
# elif cnt==5 :
#     for n in random_numbers :
#         if n==lotto_numbers[6] :
#             win = "2등"
#         else :
#             win = "3등"


# # 5. 등수 출력
# print(win)


# # 4-1. 몇 번만에 1등이 될까?
# No1_cnt = 0
# while(1) :
#     No1_cnt +=1
#     random_numbers = random.sample(range(1,46), 6)
#     random_numbers.sort()
#     if random_numbers==lotto_numbers[:6] :
#         break
# print(f"{No1_cnt}번만에 1등이 됩니다.")




'''
파이썬에는 set이라는 자료형이 있다.
list 를 set으로 형변환을 할 수 있다.
혹은 a = {1, 2, 5} 처럼 직접 만들 수 있다.
set은 중복된 값을 제거한다.
ex) a = {1, 2, 2}
set(a)
=> {1, 2}

교집합, 차집합, 합집합 을 할 수 있다.
'''

i = 0
lucky = [0, 0, 0, 0, 0]
while(1) :
    random_numbers = random.sample(range(1,46), 6)
    random_numbers.sort()
    
    matched = len(set(lotto_numbers) & set(random_numbers))
    #print(matched)

    if matched == 6 :
        lucky[0] += 1
        print(i)
        print(310000000*lucky[0] +
                66000000*lucky[1] +
                1500000*lucky[2] +
                50000*lucky[3] +
                5000*lucky[4], "원을 벌었습니다.")
        break
    elif matched == 5 and lotto_numbers[6] in random_numbers :
        lucky[1] +=1
    elif matched == 5 :
        lucky[2] +=1
    elif matched == 4 :
        lucky[3] +=1
    elif matched == 3 :
        lucky[4] +=1
    i +=1
    print(lucky, i, end="\r")



