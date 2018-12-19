#1. 구구단
# w : write(덮어쓰기), a : append(이어쓰기), r : read(읽기)


for i in range(2, 10) :
    for j in range(1, 10) :
        value = i*j

        #print(f"{i}*{j} = {value}")

'''
with open("ssafy.txt", "w") as file :
    for i in range(1,8) :
        file.write(f"{i}\n")

with open("ssafy.txt", "r") as file :
    lines = file.readlines()
    lines.sort(reverse=True)
    with open("result.txt", "w") as file2 :
        for line in lines :
            file2.write(line)

'''


'''
with open("ssafy.txt", "w") as file :
    file.write("안녕\n하세요\n저는\n한단비\n입니다\n만나서\n반갑습니다\n")

with open("ssafy.txt", "r") as file :
    lines = file.readlines()
    lines.reverse()
    with open("result.txt", "w") as file2 :
        for line in lines :
            file2.write(line)

'''
'''
with open("ssafy.txt", "w") as file :
    file.write("1\n9\n5\n3\n7\n6\n4\n")

with open("ssafy.txt", "r") as file :
    lines1 = file.readlines()
    lines2 = lines1[:]
    lines1.reverse()
    print(lines1)

    lines2.sort(reverse=True)
    print(lines2.)

    # with open("result.txt", "w") as file2 :
    #     for line in lines :
    #         file2.write(line)
'''


with open("ssafy.txt", "r") as file :
    print(type(file))
    for line in file :
        print(line.strip('\n'))