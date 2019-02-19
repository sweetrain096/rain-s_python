import sys
sys.stdin = open("1230_input.txt")
check_list = ['471034 815406 542284 170257 228297 740370 785047 677617 834173 648732',
              '364373 466241 450661 237978 437060 679163 812457 727955 262600 218437',
              '562558 606238 599072 901079 648987 991218 138805 551830 793601 911203',
              '473893 754291 376044 625502 726892 675628 577615 202218 294934 272419',
              '998955 640601 735077 815674 472787 409220 611754 821736 474544 410783',
              '477531 707563 112007 366337 887845 148402 850777 298548 383970 952541',
              '191509 619449 218830 814428 864237 528831 951407 783449 150278 484266',
              '611841 364298 772115 790896 707995 429462 335725 189113 435637 971472',
              '885312 812032 639909 338989 672494 421265 383659 140603 174105 605989',
              '660691 200576 435127 482997 733701 294859 743083 652241 756248 619607']
for tc in range(10):
    n = int(input())
    original = list(input().split())
    order_n = int(input())
    order_list = list(input().split())
    cnt = 0
    i = 0
    while cnt < order_n:
    # while cnt < 11:
        if order_list[i] == 'I':

            cnt += 1
            for plus in range(int(order_list[i + 2])):
                original.insert(int(order_list[i + 1]) + plus, order_list[i + 3 + plus])
            # print(order_list[i: i + 3 + plus + 1])
            i += 3 + plus + 1
            # print(i, cnt)
        elif order_list[i] == 'D':
            cnt += 1
            for plus in range(int(order_list[i + 2])):
                original.pop(int(order_list[i + 1]))
            # print(order_list[i: i + 3])
            i += 3
            # print(i, cnt)
        elif order_list[i] == 'A':
            cnt += 1
            for plus in range(int(order_list[i + 1])):
                original.append(order_list[i + 2 + plus])
            # print(order_list[i: i + 3 + plus])
            i += 2 + plus + 1
            # print(i, cnt)


    print(f"#{tc + 1} {' '.join(original[:10])}")

    if ' '.join(original[:10]) == check_list[tc]:
        print("정답")