def isValid(string):
    stack = []
    for i in string:
        if i in ["(", "+", "-", "*", "/"]:
            stack.append(i)
        else:
            if i == ")":
                isRen = True
                while stack[-1] != "(":
                    top = stack[-1]
                    if top == "+" or top == "-" or top == "*" or top == "/":
                        isRen = False
                    stack.pop()
                if isRen:
                    return True
                stack.pop()
    return False


if __name__ == '__main__':
    expression = input()
    res = isValid(expression)
    if res:
        print("It's Redundant")
    else:
        print("It's Not Redundant")
