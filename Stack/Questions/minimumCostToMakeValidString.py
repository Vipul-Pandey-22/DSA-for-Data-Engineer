def minimumCostToMakeValidString(string):
    if len(string) % 2 != 0:
        return -1

    stack = []
    for i in string:
        if i == '{':
            stack.append(i)
        else:

            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(i)

    a, b = 0, 0  # a = open braces, b = close braces
    while stack:
        if stack[-1] == '{':
            b += 1
        else:
            a += 1
        stack.pop()

    return (a + 1) // 2 + (b + 1) // 2


if __name__ == '__main__':
    s = input()
    result = minimumCostToMakeValidString(s)
    print(result)
    s1 = ["(", "{", "3", "}"]
