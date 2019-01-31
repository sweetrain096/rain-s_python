days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

cnt = 0
for month in range(12):
    print_month = f"{month + 1}"+" 월"
    print(f"{print_month:^20}")
    if cnt :
        print("   " * ((cnt)%7), end="")
    for day in range(days[month]):
        cnt += 1
        if day + 1 < 10:
            print("", day + 1, end=" ")
        else:
            print(day + 1, end=" ")

        if not cnt % 7:
            print()

        if day + 1 == days[month]:
            print()
































# for month in range(12):
#     print_month = f"{month + 1}"+" 월"
#     print(f"{print_month:^20}")
#     for day in range(days[month]):
#         if day + 1 < 10:
#             print("", day + 1, end=" ")
#         else:
#             print(day + 1, end=" ")
#         if not (day + 1) % 7:
#             print()
#         if day + 1 == days[month]:
#             print()