def leaders(A, N):
    # Code here
    lst = []
    A.reverse()
    li = []
    li.append(A[0])
    max1 = A[0]
    for i in range(1, N):
        if A[i] >= max1:
            li.append(A[i])
            max1 = A[i]
    li.reverse()
    return li


array = [16, 17, 4, 3, 5, 2]
print(leaders(array, len(array)))
