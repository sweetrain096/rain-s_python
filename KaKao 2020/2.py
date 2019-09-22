# p = "(()())()"
# p = ")("
p = "()))((()"



tmp = ""
def detach(test):
    right_index = []
    stack = []
    left = []
    right = []
    total = len(test)
    for now in range(total):
        # 왼쪽 괄호 => 무조건 stack
        if test[now] == '(':
            stack.append(test[now])
        # 오른쪽 괄호
        else:
            # 만약 stack이 존재하면
            if stack:
                # 그 stack의 마지막 값이 왼쪽괄호라면
                if stack[-1] == '(':
                    # 현재 오른쪽 괄호와 stack의 맨 마지막 왼쪽 괄호 left에 넣기
                    # left.append(')')
                    # left.append(stack.pop())
                    right_index.append(now)
                    stack.pop()
                # 마지막 값이 오른쪽 괄호라면
                else:
                    left = test[:now]
                    right = test[now:]
                    return left, right, right_index
            # 만약 stack이 존재하지 않으면
            # 오른쪽 괄호가 처음 나오면
            else:
                rcnt = 0
                lcnt = 0
                for right_cnt in range(now, total):
                    append_left = test[right_cnt]
                    left.append(append_left)
                    if append_left == ')':
                        rcnt += 1
                    else:
                        lcnt += 1

                    if rcnt == lcnt:
                        right = test[right_cnt + 1:]
                        return left, right, right_index

    return left, right, right_index


def make_set(arr):
    global tmp
    arr.insert(0, '(')
    print(arr)
    left, right, right_index = detach(arr)
    print(left, right, right_index)
    tmp += ''.join(arr[:right_index[-1] + 1])
    make_set(left)

def solution(p):
    test = list(p)
    answer = ''


    left, right, right_index = detach(test)


    answer += p[:right_index[-1] + 1]



    if not left and not right and right_index:
        answer = p


    print(left, right)
    make_set(left)






    print(answer)
    return answer

solution(p)