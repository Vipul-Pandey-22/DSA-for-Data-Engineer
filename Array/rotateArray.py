def reverse(arr, i, j):
    while i <= j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1


def rotateArray(arr, x):
    reverse(arr, 0, x-1)
    reverse(arr, x, len(arr)-1)
    reverse(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7]
    rotateArray(array, 2)
    print(array)
