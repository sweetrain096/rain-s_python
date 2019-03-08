import sys
sys.stdin = open("5986_input.txt")

def make_prime(check):
    prime_list = [True] * (check)
    prime_list[0] = False
    prime_list[1] = False
    m = int(check ** 0.5)
    for i in range(2, m + 1):
        if prime_list[i]:
            for j in range(2 *i, check, i):
                prime_list[j] = False
    return [i for i in range(2, check) if prime_list[i]]

def dfs():
    global cnt
    if sum(stack) > n:
        return
    print(stack)

    if len(stack) == 3 and sum(stack) == n:
        cnt += 1
        # print(stack)
    elif sum(stack) > n:
        return
    for i in primes:
        if len(stack) < 3 and (not len(stack) or stack[-1]) <= i:
            stack.append(i)
            dfs()
            stack.pop()

    return cnt

for tc in range(int(input())):
    n = int(input())
    check = n - 1
    primes = make_prime(check)
    # print(primes)
    cnt = 0
    stack = []
    print("#{} {}".format(tc + 1, dfs()))