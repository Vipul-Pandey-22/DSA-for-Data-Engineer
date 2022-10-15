def printRepeatedElement(arr):
    temp = []
    for ele_in_i in range(len(arr)):
        for ele_in_j in range(ele_in_i + 1, len(arr)):
            if arr[ele_in_i] == arr[ele_in_j]:
                print(arr[ele_in_i], end=' ')
    print()


# Optimize Way
def repeatedElement(arr):
    countDuplicate = {}
    for ele in range(len(arr)):
        if arr[ele] in countDuplicate:
            countDuplicate[arr[ele]] += 1
        else:
            countDuplicate[arr[ele]] = 1

    for key, val in countDuplicate.items():
        if val > 1:
            print(key, end=' ')


if __name__ == '__main__':
    duplicateElement = [4, 2, 4, 5, 2, 3, 1]
    printRepeatedElement(duplicateElement)
    print("Optimized Code's Result")
    repeatedElement(duplicateElement)



