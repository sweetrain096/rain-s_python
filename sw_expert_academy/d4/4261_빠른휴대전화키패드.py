import sys
sys.stdin = open("4261_input.txt")

keypad = dict()
keypad['a'] = 2
keypad['b'] = 2
keypad['c'] = 2
keypad['d'] = 3
keypad['e'] = 3
keypad['f'] = 3
keypad['g'] = 4
keypad['h'] = 4
keypad['i'] = 4
keypad['j'] = 5
keypad['k'] = 5
keypad['l'] = 5
keypad['m'] = 6
keypad['n'] = 6
keypad['o'] = 6
keypad['p'] = 7
keypad['q'] = 7
keypad['r'] = 7
keypad['s'] = 7
keypad['t'] = 8
keypad['u'] = 8
keypad['v'] = 8
keypad['w'] = 9
keypad['x'] = 9
keypad['y'] = 9
keypad['z'] = 9


for tc in range(int(input())):
    s, N = input().split()
    n = int(N)
    words = input().split()
    cnt = 0
    for word in words:
        flag = True
        for i in range(len(word)):
            if (keypad[word[i]] != int(s[i])):
                flag = False
                break
        if flag:
            cnt += 1

    print(f"#{tc + 1} {cnt}")
