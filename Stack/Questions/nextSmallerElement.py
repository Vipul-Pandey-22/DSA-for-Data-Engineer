def nextSmallerElement(arr):
    stack = [-1]
    ans = [None]*len(arr)

    for i in range(len(arr)-1, -1, -1):

        curr = arr[i]

        while stack[-1] >= curr:
            stack.pop()

        ans[i] = stack[-1]
        stack.append(curr)

    return ans


if __name__ == '__main__':
    array = [2, 1, 4, 3]
    result = nextSmallerElement(array)
    print(result)



