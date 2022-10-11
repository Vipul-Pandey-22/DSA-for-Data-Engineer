def sortZerosAndOnes(arr):
    sorted_array = []
    count_0 = 0
    count_1 = 0
    for ele in arr:
        if ele == 0:
            count_0 += 1
        else:
            count_1 += 1

    for ele in range(count_0):
        sorted_array.append(0)
    for ele in range(count_1):
        sorted_array.append(1)

    return sorted_array


inputArray = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
result = sortZerosAndOnes(inputArray)
print(result)
