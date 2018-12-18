file = open("new.txt", "w")
file.write("글 써졌나??")
file.close()

#1.파일 쓰기
with open("new1.txt", "w") as file :
    '''
    파이썬에서 with는 컨택스트 매니저라고 부른다. 파일을 열고 닫을 때만 사용한다.
    with 블록 내에서 파일을 조작하고, 블록이 끝나게 되면 file.close()가 된다.
    '''
    file.write("글 또 쓰자!")

#2. 파일 읽기
with open("new.txt", "r") as file :
    line = file.read()
    print(line)

#3. 파일 여러줄 쓰기 new2.txt
with open("new2.txt", "w") as file :
    for line in range(50):
        file.write(f"{line}번 째 줄입니다. 단비야 힘내!!\n")

#4. 파일 여러줄 읽기
with open("new2.txt", "r") as file :
    '''
    while (1) :
        
        if line=="" :
            break
        
        line = file.readline()
        #readline()의 type은 str
        print(line)
    '''
    lines = file.readlines()
    #readlines()의 type은 list
    #print(lines)
    for line in lines :
        print(line)


