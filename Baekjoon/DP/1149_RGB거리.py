import sys
sys.stdin = open("1149_input.txt")
def make_price(n):
    price_list = [rgb_list[0]]

    if n == 1:
        return min(price_list[n - 1])
    for i in range(1, n):
        num1 = rgb_list[i][0] + min(price_list[i - 1][1], price_list[i - 1][2])
        num2 = rgb_list[i][1] + min(price_list[i - 1][0], price_list[i - 1][2])
        num3 = rgb_list[i][2] + min(price_list[i - 1][0], price_list[i - 1][1])

        price_list.append([num1, num2, num3])

    return min(price_list[n - 1])


n = int(input())
rgb_list = []
for i in range(n):
    rgb_list.append(list(map(int, input().split())))

# print(rgb_list)

result = make_price(n)
print(result)