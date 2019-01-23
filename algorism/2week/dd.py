lists = [[i for i in range(1, 101)] for i in range(1, 101)]
cross = []
for i in range(1):
    print(list(map(list, zip(*lists)))[i])
#     zipped = zip(*lists)
# print(list(map(list, zipped))[i])