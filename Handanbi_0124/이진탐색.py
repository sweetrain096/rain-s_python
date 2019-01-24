import sys
sys.stdin = open("sample3_input.txt")

for t in range(int(input())):
    total, Pa, Pb = list(map(int, input().split()))
    La, Lb, Ra, Rb = 1, 1, total, total
    result = ""
    i = 0
    while True:
        Ca, Cb = int((Ra+La) / 2), int((Rb+Lb) / 2)
        if Pa == Ca and Pb == Cb :
            result = "0"
            break
        elif Pa == Ca :
            result = "A"
            break
        elif Pb == Cb :
            result = "B"
            break

        if Ca > Pa :
            Ra = Ca
        else :
            La = Ca

        if Cb > Pb:
            Rb = Cb
        else :
            Lb = Cb

    print(f"#{t + 1} {result}")