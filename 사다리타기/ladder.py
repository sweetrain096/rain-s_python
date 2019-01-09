import random

people = input("사람 이름을 띄어쓰기 해서 입력해주세요 : ").split(" ")
n = int(input("몇 명을 고를건가요? : "))

#print(len(people))

select = random.sample(people, n)
select = " ".join(list(map(str, select)))


print(select)