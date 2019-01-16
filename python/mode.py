test_count = int(input())
for tests in range(test_count):
    test_number = int(input())
    lists = [0] * 101
    score_list = list(map(int, input().split()))
    result = 0
    for score in score_list:
        lists[score] +=1

    max_result = max(lists)

    for check in range(100):
        if lists[check - 1] == max_result :
            result = lists.index(lists[check - 1])
            lists[check - 1] = 0
    print(f"#{test_number} {result}")