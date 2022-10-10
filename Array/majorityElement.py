# Brute Force Approach
def bruteApproach(arr):  # [3, 1, 2, 3, 3]
    maxRepeatedElement = 0
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                cnt += 1
            if maxRepeatedElement < cnt:
                maxRepeatedElement = cnt
        cnt = 0
    if maxRepeatedElement > len(arr) // 2:
        print(maxRepeatedElement)
        return


# Hash Map Technique
def majorityElement(arr):
    countFreq = {}
    value = 0
    for i in arr:
        if i in countFreq:
            countFreq[i] += value + 1
        else:
            countFreq[i] = value + 1

    for key, val in countFreq.items():
        if val > len(arr) // 2:
            print(key)
            print(val)
            return


# Moore's Voting Algorithm
def optimalApproachForMajorityElement(arr):
    candidate = -1
    votes = 0
    for i in arr:
        if votes == 0:
            candidate = i
            votes = 1
        elif i == candidate:
            votes += 1
        else:
            votes -= 1

    cnt = 0
    for i in arr:
        if i == candidate:
            cnt += 1

    if cnt > len(arr) // 2:
        print(candidate)
        print(cnt)


if __name__ == '__main__':
    array = [3, 3, 4, 4, 4]
    optimalApproachForMajorityElement(array)
    print()
    majorityElement(array)
    # print("Hash Map's Solution Result :", res)
    print()
    bruteApproach(array)
    # print("Brute Force Solution Result :", bruteForceResult)

