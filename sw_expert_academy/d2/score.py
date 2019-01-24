import sys
sys.stdin = open("score_input.txt")

for t in range(int(input())):
    score_list = []
    score_check = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    n, k = list(map(int, input().split()))
    result = [0] * n
    for student in range(n):
        score = list(map(int, input().split()))
        total = round(score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.20, 1)
        score_list.append(total)


    for i in range(n):
        max_index = i
        for j in range(n):
            if score_list[max_index] < score_list[j]:
                max_index = j
        score_list[max_index] = -1
        result[max_index] = int(i // (n / 10))



    print(f"#{t + 1} {score_check[result[k-1]]}")
