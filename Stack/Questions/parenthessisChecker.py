def isValid(x):
    stack = []
    # edge case 1
    if x[0] in [")", "}", "]"]:
        return False

    if x[len(x)-1] in ["[", "(", "{"]:
        return False
    for i in x:
        if i in ["(", "{", "["]:
            stack.append(i)
        else:
            curr_char = stack.pop()
            if curr_char == "(":
                if i != ")":
                    return False
            if curr_char == "{":
                if i != "}":
                    return False
            if curr_char == "[":
                if i != "]":
                    return False

    if stack:
        return False
    return True


check = ")[[[]]()(){}("
print(isValid(check))
