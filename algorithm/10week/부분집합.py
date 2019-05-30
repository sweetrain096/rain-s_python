def powerset(n, k):
    if n == k:
        for i in range(n):
            if A[i]:
                print(data[i], end=" ")
            else:
                print(" ", end=" ")
        print()
    else:
        A[k] = 1
        powerset(n, k + 1)
        A[k] = 0
        powerset(n, k + 1)


n = 3
A = [0] * n
data = [1, 2, 3]

powerset(n, 0)