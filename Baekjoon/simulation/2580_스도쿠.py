import sys
sys.stdin = open("2580_input.txt")


board = []
for _ in range(9):
    board.append(list(map(int, input().split())))

rows = dict()
cols = dict()
squares = dict()

for i in range(9):
    vr = [0 for _ in range(10)]
    vc = [0 for _ in range(10)]
    for j in range(9):
        vr[board[i][j]] = 1
        vc[board[j][i]] = 1
    tr = []
    tc = []
    for k in range(1, 10):
        if not vr[k]:
            tr.append(k)
        if not vc[k]:
            tc.append(k)
    rows[i] = tr
    cols[i] = tc
# print(rows)
# print(cols)


for r in range(3):
    for c in range(3):
        visited = [0 for _ in range(10)]
        for nr in range(r*3, r*3 + 3):
            for nc in range(c*3, c*3 + 3):
                if board[nr][nc]:
                   visited[board[nr][nc]] = 1
        temp = []
        for i in range(1, 10):
            if not visited[i]:
                temp.append(i)
        squares[(r, c)] = temp
# print(squares)

stack = []
for r in range(9):
    for c in range(9):
        if not board[r][c]:
            stack.append((r, c))
# print(stack)

while stack:
    r, c = stack.pop(0)
    sr = r//3
    sc = c//3
    # print(r, c)
    # for line in board:
    #     print(line)
    val = 0
    if rows.get(r) and len(rows[r]) == 1:
        val = rows.pop(r)[0]
    elif cols.get(c) and len(cols[c]) == 1:
        val = cols.pop(c)[0]
    elif squares.get((sr, sc)) and len(squares[(sr, sc)]) == 1:
        val = squares.pop((sr, sc))[0]

    if not val:
        stack.append((r, c))
        continue
    board[r][c] = val

    if rows.get(r):
        if len(rows[r]) == 1 and val in rows[r]:
            rows.pop(r)
        elif val in rows[r]:
            rows[r].remove(val)
    if cols.get(c):
        if len(cols[c]) == 1 and val in cols[c]:
            cols.pop(c)
        elif val in cols[c]:
            cols[c].remove(val)
    if squares.get((sr, sc)):
        if len(squares[(sr, sc)]) == 1 and val in squares[(sr, sc)]:
            squares.pop((sr, sc))
        elif val in squares[(sr, sc)]:
            squares[(sr, sc)].remove(val)



for line in board:
    print(' '.join(map(str, line)))
