print("hello world")


#1~100까지의 숫자를

#even list를 만들어 짝수만 저장

#odd list를 만들어 홀수만 저장
evenlist = []
oddlist = []

for i in range(1, 101) :
    if i%2==0 :
        
        evenlist.append(i)
    else :
        oddlist.append(i)

print(evenlist)
print(oddlist)

