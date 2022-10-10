def isPairExists(lst, Sum):
    Map = {}
    for idx in range(len(lst)):
        remainingElement = Sum - lst[idx]
        if remainingElement in Map:
            return True
        Map[lst[idx]] = idx
    return False


if __name__ == '__main__':
    arr = [1, 4, 45, 6, 10]
    value = 17
    result = isPairExists(arr, value)
    if result:
        print("yes")
    else:
        print("No")
