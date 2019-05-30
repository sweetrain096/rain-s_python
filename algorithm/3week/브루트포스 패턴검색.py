def brute_force(p, t):
    i, j = 0, 0     # t, p의 인덱스
    m = len(p)      # 찾을 패턴의 길이
    n = len(t)      # 전체 텍스트의 길이
    while j < m and i < n:
        if t[i] != p[j]:
            i -= j
            j = -1

        i += 1
        j += 1
    if j == m:
        return i - m    # 검색 성공 시 몇번째에 발견했나?
    else :
        return -1       # 검색 실패

t = "TTTTA"     # 검색될 문자열
p = "TTA"       # 검색할 문자열
print(brute_force(p, t))
print(t.find(p))