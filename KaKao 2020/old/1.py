# s = "aabbaccc"
# s = "ababcdcdababcdcd"
# s = "abcabcdede"
# s = "abcabcabcabcdededededede"
s = "xababcdcdababcdcd"



def solution(s):
    max_len = len(s)
    answer = max_len

    for i in range(1, int(max_len/2) + 1):
        tmp = []
        text = s
        now = 0
        while text:
            # print(text[now:now + i], text[now + i: now + i + i])
            if text[now:now+i] == text[now+i:now+i+i]:
                if not tmp:
                    tmp.append(2)
                    tmp.append(text[now:now+i])
                elif tmp[-1] != text[now:now+i]:
                    tmp.append(2)
                    tmp.append(text[now:now+i])
                else:
                    tmp[-2] += 1
                text = text.replace(text[now:now+i], "", 1)
            else:
                if not tmp:
                    tmp.append(text[now:now + i])
                elif tmp[-1] != text[now:now+i]:
                    tmp.append(text[now:now+i])
                text = text.replace(text[now:now + i], "", 1)
            # print(text)
            # print(tmp)
        result = ''.join(map(str, tmp))
        # print(result)
        if len(result) < answer:
            answer = len(result)




    # print(answer)
    return answer

solution(s)