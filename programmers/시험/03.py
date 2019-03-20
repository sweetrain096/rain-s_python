import sys
sys.stdin = open("03_input.txt")

n = int(input())
table1 = []
for i in range(n):
    tmp = list(input().split())
    table1.append(tmp)
table1 = [table1[0]] + sorted(table1[1:])



m = int(input())
table2 = []
for i in range(m):
    tmp = list(input().split())
    table2.append(tmp)
table2 = [table2[0]] + sorted(table2[1:])



for i in table1:
    flag = False
    for j in range(m):
        if i[0] == table2[j][0]:
            i += table2[j][1:]
            flag = True
    if not flag:
        i += ['NULL', 'NULL']




for i in table1:
    print(' '.join(i))