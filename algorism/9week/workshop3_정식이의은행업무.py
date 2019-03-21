import sys
sys.stdin = open("workshop3_input.txt")

for tc in range(int(input())):
    bit2 = list(input())
    bit3 = list(input())
    result = -1

    bit2_list = []
    for i in range(len(bit2)):
        tmp = bit2[:]
        if bit2[i] == '1':
            tmp[i] = '0'
        else:
            tmp[i] = '1'
        bit2_list.append(int(''.join(tmp),2))
    # print(bit2_list)

    list3 = ['0', '1', '2']
    for i in range(len(bit3)):
        tmp = bit3[:]

        for j in list3:
            if bit3[i] != j:
                tmp[i] = j
                a = set(bit2_list)
                total = len(a)
                int_3 = int(''.join(tmp), 3)
                # a += set(int_3)
                if len(a|set([int_3])) == total:
                    result = int_3
                    break
        if result != -1:
            print("#{} {}".format(tc + 1, result))
            break