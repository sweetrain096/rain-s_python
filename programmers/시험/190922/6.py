import sys
sys.stdin = open("6_input.txt")

def print_c(n, start_r, len_r, char):
    if char == '1':
        for line in range(max_r):
            if line < start_r or line >start_r + len_r-1:
                result[line].append('.' * n)
            elif line >= start_r:
                result[line].append('.' * (n-1) + '#')

    elif char == '2':
        for line in range(max_r):
            if line < start_r or line > start_r + len_r -1:
                result[line].append('.' * n)
            elif line == start_r or line == start_r + n-1 or line == start_r + len_r - 1:
                result[line].append('#' * n)
            elif line < start_r + n-1:
                result[line].append('.' * (n-1) + '#')
            else:
                result[line].append('#' + '.' * (n-1))

    elif char == '3':
        for line in range(max_r):
            if line == start_r or line == start_r + n-1 or line == start_r + len_r - 1:
                result[line].append('#' * n)
            elif line < start_r or line > start_r + len_r -1:
                result[line].append('.' * n)
            else:
                result[line].append('.' * (n-1) + '#')
    elif char == '4':
        for line in range(max_r):
            if line < start_r or line > start_r + len_r -1:
                result[line].append('.' * n)
            elif line < start_r + n-1:
                result[line].append('#' + '.' * (n-2) + '#')
            elif line == start_r + n-1:
                result[line].append('#'*n)
            else:
                result[line].append('.' * (n-1) + '#')
    elif char == '5':
        for line in range(max_r):
            if line < start_r or line > start_r + len_r - 1:
                result[line].append('.' * n)
            elif line == start_r or line == start_r + n - 1 or line == start_r + len_r - 1:
                result[line].append('#' * n)
            elif line < start_r + n - 1:
                result[line].append('#' + '.' * (n - 1))
            else:
                result[line].append('.' * (n - 1) + '#')
    elif char == '6':
        for line in range(max_r):
            if line < start_r or line > start_r + len_r - 1:
                result[line].append('.' * n)
            elif line < start_r + n - 1:
                result[line].append('#' + '.' * (n-1))
            elif line == start_r + n - 1 or line == start_r + len_r - 1:
                result[line].append('#' * n)
            else:
                result[line].append('#'+'.' * (n - 2) + '#')
    elif char == '7':
        for line in range(max_r):
            if line < start_r or line >start_r + len_r-1:
                result[line].append('.' * n)
            elif line == start_r:
                result[line].append('#' * n)
            elif line > start_r:
                result[line].append('.' * (n-1) + '#')

    elif char == '8':
        for line in range(max_r):
            if line < start_r or line > start_r + len_r - 1:
                result[line].append('.' * n)
            elif line == start_r or line == start_r + n - 1 or line == start_r + len_r - 1:
                result[line].append('#' * n)
            else:
                result[line].append('#' + '.' * (n - 2) + '#')
    elif char == '9':
        for line in range(max_r):
            if line < start_r or line > start_r + len_r - 1:
                result[line].append('.' * n)
            elif line == start_r or line == start_r + n - 1:
                result[line].append('#' * n)
            elif line < start_r + n - 1:
                result[line].append('#' + '.' * (n - 2) + '#')
            else:
                result[line].append('.' * (n - 1) + '#')
    else:
        for line in range(max_r):
            if line < start_r or line > start_r + len_r - 1:
                result[line].append('.' * n)
            elif line == start_r or line == start_r + len_r - 1:
                result[line].append('#' * n)
            else:
                result[line].append('#' + '.' * (n - 2) + '#')

n, check_type = input().split()
n = int(n)
data = []
max_c = 0
for i in range(n):
    data.append(list(map(int, input().split())))
    if data[i][0] > max_c:
        max_c = data[i][0]

max_r = 2 * max_c - 1

result = [[] for _ in range(max_r)]

for i in data:
    n, num = i
    len_r = 2 * n - 1
    if check_type == 'TOP':
        start_r = 0
    elif check_type == 'MIDDLE':
        start_r = (max_r - len_r)/2
    else:
        start_r = max_r - len_r

    for char in str(num):
        print_c(n, start_r, len_r, char)

for i in result:
    print(' '.join(i))