def right_str(s):
    total = 0
    flag = True
    for i in range(len(s)):
        if s[i] == '(':
            total += 1
        else:
            if total:
                total -= 1
            else:
                flag = False
                break
    if flag:    # 올바른 문자열
        return True
    return False


def solution(p):
    if p == '':
        return ''

    if right_str(p):
        return p

    total = 0
    for i in range(len(p)):
        if p[i] == '(':
            total += 1
        else:
            total -= 1
        if not total:
            u = p[:i+1]
            v = p[i+1:]
            break
    if right_str(u):
        return u+solution(v)

    temp = "("
    temp += solution(v)
    temp += ")"
    # print("temp", temp)
    for i in range(1, len(u) - 1):
        if u[i] == '(':
            temp += ')'
        else:
            temp += '('
    return temp






    # answer = ''
    # return answer



ps = ["(()())()",
      ")(",
      "()))((()"]

for p in ps:
    print(solution(p))