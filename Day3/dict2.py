"""
파이썬 dictionary 활용 기초!
"""

# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}

score = 0

# 답변 코드는 아래에 작성해주세요.
print("=====Q1=====")
for value in iu_score.values() :
    score = score+value
print(score/len(iu_score))





# 2. 반 평균을 구하세요.
score = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}
# 답변 코드는 아래에 작성해주세요.
print("=====Q2=====")
avr = 0
total = 0
for person in score.values() :
    #print(person)
    for value in person.values() :
        avr = avr+value
        total = total+1
print(avr/total)




# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
city = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q3=====")

for key, value in city.items() :
    print(f"{key} : {sum(value)/len(value)}")


# 답변 코드는 아래에 작성해주세요.
print("=====Q3-1=====")
# th = 0
# city_th = {}
# for key, value in city.items() :
#     th = sum(value)/len(value)
#     city_th[key] = th
#     #city[key].append(th)
# print(city_th)
# dict_min = min(city_th.keys(), key=(lambda k: city_th[k]))
# print(dict_min)
# dict_max = max(city_th.keys(), key=(lambda k: city_th[k]))
# print(dict_max)

hot = 0
cold = 0

# for key, value in city.items() :
#     for i in value :
#         #print(key, i)
#         if hot<=i :
#             hot = i
#             max_city = key
#         if cold>=i :
#             cold = i
#             min_city = key
cnt = 0

for key, value in city.items():
    if cnt == 0:
        hot = max(value)
        cold = min(value)
        min_city = key
        max_city = key
    else :
        if (min(value)<cold) :
            cold = min(value)
            min_city = key
        elif max(value) > hot :
            hot = max(value)
            max_city = key
    cnt +=1

print(f"가장 따뜻한 곳은 {max_city}입니다.")
print(f"가장 추운 곳은 {min_city}입니다.")




# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.
print("=====Q4=====")
if (2 in city["서울"]):
    print("서울은 영상 2도였던적이 있습니다.")
else : 
    print("서울은 영상 2도였던적이 없습니다.") 



# a=[1,2,4]
# 3 in a
# #출력결과 : False