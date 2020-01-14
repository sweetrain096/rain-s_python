import sys
sys.stdin = open("7675_input.txt")

def is_upper(alpha):
    if ord(alpha) >= ord('A') and ord(alpha) <= ord('Z'):
        return True
    return False

def is_lower(alpha):
    if ord(alpha) >= ord('a') and ord(alpha) <= ord('z'):
        return True
    return False

for tc in range(int(input())):
    n = int(input())
    sentense = input().split()
    results = []

    result = []
    for word in sentense:
        if not is_upper(word[0]):
            if not word[-1] in ['.', '!', '?']:
                continue
            results.append(len(list(result)))
            result = []
            continue
        is_ture = True
        for i in range(1, len(word)):
            if i == len(word) - 1 and word[-1] in ['.', '!', '?']:
                break
            if not is_lower(word[i]):
                is_ture = False
                break
        if is_ture:
            result.append(word)
        if word[-1] in ['.', '!', '?']:
            results.append(len(list(result)))
            result = []
    print(f"#{tc + 1} {' '.join(map(str, results))}")
