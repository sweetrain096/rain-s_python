def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        pivot = 0
        cnt = 0
        while pivot < len(s) - i - 1:
            check = s[pivot:pivot+i]
            cc = 0
            check_pivot = pivot+i
            while check_pivot < len(s) - i + 1:
                flag = True
                for j in range(i):
                    if check[j] != s[check_pivot + j]:
                        flag = False
                if flag:
                    cc += 1
                    check_pivot += i
                else:
                    break
            if cc:
                cnt += len(str(cc+1))
                cnt += i
                pivot = check_pivot
            else:
                pivot += i
                cnt += i
        cnt += len(s) - pivot
        if answer > cnt:
            answer = cnt

    return answer


print(solution("ababcdcdababcdcd"))