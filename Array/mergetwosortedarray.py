array1 = [1, 3, 5, 7, 9]
array2 = [2, 4, 6]
array3 = [None]*(len(array1) + len(array2))


def merge(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    n = len(arr1) - 1
    m = len(arr2) - 1

    while i <= n and j <= m:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1
        else:
            arr3[k] = arr2[j]
            j += 1
        k += 1

    while i <= n:
        arr3[k] = arr1[i]
        i += 1
        k += 1

    while j <= m:
        arr3[k] = arr2[j]
        k += 1
        j += 1


def print_ans(ans):
    for i in ans:
        print(i, end=" ")


merge(array1, array2, array3)
print_ans(array3)

