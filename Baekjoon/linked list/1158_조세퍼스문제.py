import sys
sys.stdin = open("1158_input.txt")

n, m = map(int, input().split())
origin_list = [i for i in range(1, n + 1)]
result = []
rp = 0
while origin_list:
    if rp + m - 1 < len(origin_list):
        rp += (m - 1)
        result.append(origin_list.pop(rp))
    else:
        rp += (m - 1)
        # print(rp, len(origin_list))
        while rp >= len(origin_list):

            rp -=len(origin_list)

        result.append(origin_list.pop(rp))
    # print(result, origin_list, rp)

print("<", end="")
for i in range(n):
    if i != n - 1:
        print(result[i], end=", ")
    else:
        print(result[i], end="")
print(">")
# print("<{}>".format(result))