import sys
sys.stdin = open("5293_string.txt")

def find():
    return 0


for test_case in range(int(input())):
    check_list = ['00', '01', '10', '11']
    result = []
    input_data = list(map(int, input().split()))

    input_index = 0
    while True :
        if not result:
            if input_data[input_index] :
                result.append(check_list[input_index])
                input_data[input_index] -= 1
            else :
                input_index += 1
        else :
            if input_data[input_index] and result[-1][-1] == check_list[input_index][0]:
                result.append(check_list[input_index])
                input_data[input_index] -= 1
            else :
                input_index += 1



        if input_index == 4 :
            input_index = 0

    print(f"#{test_case + 1} {result}")