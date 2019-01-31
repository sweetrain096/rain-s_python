import sys
sys.stdin = open("input1.txt")

for test_case in range(int(input())):
    str1 = input()
    str2 = input()
    length = len(str1)

    index = 0
    i = 1
    result = 0
    while True:
        if str1[-i] == str2[index: index + length][-i]:
            i += 1
            if i == length + 1:
                result = 1
                break
        else :
            i = 1
            if (index + length) == len(str2):
                break
            check = 0
            for cnt in range(2, length + 1):
                if str2[index: index + length][-i] == str1[-(cnt)]:
                    index += (cnt - 1)
                    check += 1
                    break

            if cnt == length and check == 0:
                index += length
            if index + length > len(str2) :
                index -= (index + length - len(str2))




    print(f"#{test_case + 1} {result}")




