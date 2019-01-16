T = int(input())
for i in range(T) :
    N = int(input())
    numbers = list(map(int, input().split()))
    result = 0
    max = numbers[-1]
    for j in range(N, 1, -1):
        if max >= numbers[j-2] :
            result += max - numbers[j - 2]
        else :
            max = numbers[j-2]

    print(f"#{i+1} {result}")


    10
    KOREAKOREAKOREAKOREAKOREAKOREA
    SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA
    GALAXYGALAXYGALAXYGALAXYGALAXY
    EXOEXOEXOEXOEXOEXOEXOEXOEXOEXO
    B1A4B1A4B1A4B1A4B1A4B1A4B1A4B1
    APINKAPINKAPINKAPINKAPINKAPINK
    BLACKPINKBLACKPINKBLACKPINKBLA
    TWICETWICETWICETWICETWICETWICE
    REDVELVETREDVELVETREDVELVETRED
    ABCABCABCABCABCABCABCABCABCABC