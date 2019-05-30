def perm(n, r):
    if r == 0:
        print(a)
    else:
        for i in range(n - 1, -1, -1):
            a[i], a[n - 1] = a[n - 1], a[i]
            t[r - 1] = a[n - 1]
            perm(n - 1, r - 1)
            a[i], a[n - 1] = a[n - 1], a[i]


a = [1, 2, 3]
t = [0] * 3

perm(3, 3)