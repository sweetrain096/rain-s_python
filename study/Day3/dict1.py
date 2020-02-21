phonebook = {
    #key : value
    "중국집" : "11111",
    "초밥집" : "22222",
    "한식집" : "33333"
}
#딕셔너리에서 키값에는 리스트 딕셔너리를 제외한 모든 값 들어갈 수 있다.
#딕셔너리 밸류값에는 리스트 딕셔너리까지 들어갈 수 있다.

phonebook2 = dict(중국집=1, 초밥집=2)

# print(phonebook)
# print(phonebook2)

phonebook["분식집"] = "44444"
# print(phonebook)



# # 1. 좋아하는 그룹 : key-이름, value-나이

# Red_Velvet = {
#     "웬디" : 25,
#     "아이린" : 28,
#     "슬기" : 25,
#     "조이" : 23,
#     "예리" : 20
# }

# # 2. idol : key - 그룹명, value : dictionary
# idol = {
#     "redvelvet" : {
#         "아이린" : 28,
#         "슬기" : 25
#     },
#     "exo" :{
#         "백현" : 27,
#         "찬열" : 27
#     }
# }

# print(Red_Velvet)
# print(idol)



for key in phonebook :
    print(key, end = " ") #key가 출력된다. value가 들어가면 key를 찾을 수 없지만, key가 들어가면 value를 뽑을 수 있다.
    # end = " "로 만들면 출력시 enter가 입력되지 않고, 띄어쓰기 하나만으로 표현된다.
    print(phonebook[key])

for key, value in phonebook.items() :
    print(key, value)
#변수의 이름은 바뀌어도 상관 없다. 그러나 앞의 변수에는 key, 뒤의 변수에는 value가 들어간다.

for value in phonebook.values() :
    print(value)
for key in phonebook.keys() :
    print(key)