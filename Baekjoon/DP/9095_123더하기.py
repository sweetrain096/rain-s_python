import sys
sys.stdin = open("9095_input.txt")
def make_sum(n):

    for i in range(5, n + 1):
        sum_data.append(sum(sum_data[-3:]))
        results.append(results[i - 1] + sum_data[i - 1])
    return results[n]



for tc in range(int(input())):
    sum_data = [0, 1, 2, 3]
    results = [0, 1, 2, 4, 7]
    n = int(input())
    if n <= 3:
        result = results[n]
    else:
        result = make_sum(n)

    # print(sum_data, results)
    print(result)
