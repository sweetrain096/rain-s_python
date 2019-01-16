testcase = int(input())
lists = []
graph = {}
for test_num in range(testcase):
    N = int(input())
    for i in range (N) :
        lists.append(input().split())
    thief, police = list(map(int, input().split()))

    print(lists)
