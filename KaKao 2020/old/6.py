n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]


# def find_weak(arr, cnt_n):
#     find_cnt = 0
#     find_result = []
#     for i in range(len(arr)):
#         now_find = 0
#         test = arr[:]
#         if test[i]:
#



def solution(n, weak, dist):
    answer = 0
    data = [0 for _ in range(n)]
    weak_diff = []

    total_weak = len(weak)
    for i in range(len(weak)):
        data[weak[i]-1] = 1

        now = weak[i]

        if not i:
            left = weak[-1]
            right = weak[i + 1]
            # 왼쪽이 작거나 같으면 = 1
            if n - left + now < right - now:
                min_diff = n - left + now
                ro = 1
            # 오른쪽이 작으면 = 0
            else:
                min_diff = right - now
                ro = 0
            weak_diff.append([min_diff, i, ro])
        elif i == len(weak) - 1:
            left = weak[i-1]
            right = weak[0]
            if now - left < n-now + right:
                min_diff = n - now - left
                ro = 1
            # 오른쪽이 작으면 = 0
            else:
                min_diff = n-now + right
                ro = 0
            weak_diff.append([min_diff, i, ro])
        else:
            left = weak[i-1]
            right = weak[i+1]
            if now - left < right - now:
                min_diff = now - left
                ro = 1
            # 오른쪽이 작으면 = 0
            else:
                min_diff = right - now
                ro = 0
            weak_diff.append([min_diff, i, ro])



    weak_diff.sort(key=lambda weak_diff:weak_diff[0])
    print(weak, weak_diff)

    dist.sort()

    find_weak = 0
    for friend in range(len(dist)-1, -1, -1):
        print(dist[friend])









    return answer


solution(n, weak, dist)