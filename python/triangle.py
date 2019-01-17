T = int(input())
for test_case in range(T):
    N = int(input())
    print_list = []
    new_list = []
    print(f"#{test_case+1}")
    for play in range(1, N + 1):

        if play == 1 :
            print_list = ["1"]
            print(" ".join(print_list))
        elif play == 2 :
            print_list = ["1","1"]
            print(" ".join(print_list))
        else :
            for i in range(play-2):
                new_list.append(str(int(print_list[i]) + int(print_list[i+1])))
            new_list.insert(0, "1")
            new_list.append("1")
            print(" ".join(new_list))
            print_list = new_list
            new_list = []
