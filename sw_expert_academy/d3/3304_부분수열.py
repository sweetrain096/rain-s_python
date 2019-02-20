import sys
sys.stdin = open("3304_input.txt")

for tc in range(int(input())):
    str1, str2 = input().split()
    if len(str1) < len(str2):
        str1, str2 = str2, str1
    total = len(str1)
    cnt1, cnt2 = 0, 0
    result = 0

    for cnt1 in range(total):
        common = ""
        cnt2 = 0
        for char1 in range(cnt1, len(str1)):
            for char2 in range(cnt2, len(str2)):
                if str1[char1] == str2[char2]:

                    common += str1[char1]
                    cnt2 = char2
                    break
        if result < len(common):
            result = len(common)
        # print(common, len(common))

    print(f"#{tc + 1} {result}")