import sys
sys.stdin = open("3813_input.txt")

for tc in range(int(input())):
    n, k = map(int, input().split())
    w_list = list(map(int, input().split()))
    k_list = list(map(int, input().split()))

    
    print(f"{tc + 1} ")