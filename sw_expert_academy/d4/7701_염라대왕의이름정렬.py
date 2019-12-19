import sys
sys.stdin = open("7701_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    len_dict = dict()
    for i in range(N):
        name = input()
        if len_dict.get(len(name)):
            len_dict[len(name)].append(name)
        else:
            len_dict[len(name)] = [name]


    print(f"#{tc + 1}")
    for i in range(1, 51):
        data = len_dict.get(i)
        if data:
            data = list(set(data))
            for j in sorted(data):
                print(j)











'''
def make_len_index(new_len, index, max_len):
    if len_index[new_len] == -1:
        len_index[new_len] = index
    for i in range(new_len+1, max_len + 1):
        if len_index[i] != -1:
            len_index[i] += 1

T = int(input())

for tc in range(T):
    N = int(input())
    data = []
    len_index = [-1 for _ in range(51)]
    max_len = 0
    for i in range(N):
        name = input()
        if not data:
            data.append(name)
            make_len_index(len(data), 0, len(data))
            max_len = len(data)
        else:
            flag = False
            start = len_index[len(name)] - 1
            end = len_index[len(name)+1] + 1
            if start <= -1:
                start = 0
            if end == 0:
                end = len(data)

            for j in range(start, end):
                if len(name) < len(data[j]):
                    data.insert(j, name)
                    flag = True
                    make_len_index(len(name), j, max_len)
                    break
                if len(name) == len(data[j]):

                    if name == data[j]:
                        flag = True
                        break
                    if name < data[j]:
                        data.insert(j, name)
                        flag = True
                        make_len_index(len(name), j, max_len)
                        break
            if not flag:
                data.append(name)
                if max_len < len(name):
                    max_len = len(name)
                make_len_index(len(name), end, max_len)

    print(f"#{tc + 1}")
    for i in data:
        print(i)
'''

'''
for tc in range(T):
    N = int(input())
    name_dict = dict()
    for i in range(N):
        name = input()
        if not name_dict.get(name):
            name_dict[name] = len(name)
    print(f"#{tc+1}")
    print(name_dict)
    # print(data)
    for datum in name_dict:
        print(datum)
'''

