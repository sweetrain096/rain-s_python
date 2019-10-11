a = 5
b = 24

days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
def solution(a, b):
    cnt = 5 #fri
    cnt += sum(days[:a])
    cnt += b-1
    find_day = cnt % 7
    answer = day[find_day]

    return answer

print(solution(a, b))