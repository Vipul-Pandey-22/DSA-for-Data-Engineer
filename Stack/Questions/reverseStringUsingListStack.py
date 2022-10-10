def reverseStack(string):
    stack = []
    ans = ""
    i = 0
    for i in string:
        stack.append(i)

    for i in range(len(string)-1, -1, -1):
        ans += str(string[i])
    return ans


userInput = input()
result = reverseStack(userInput)
print(result)
