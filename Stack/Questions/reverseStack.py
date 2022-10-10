# def reverseStack(S):
#     newStack = []
#     length = len(S)
#     while length:
#         temp = S.pop()
#         newStack.append(temp)
#         length -= 1
#     return newStack


def insertAtBottom(S, data):
    if not S:
        S.append(data)
        return

    temp = S[-1]
    S.pop()
    insertAtBottom(S, data)
    S.append(temp)


def stack(S):
    if not S:
        return

    temp = S.pop()
    stack(S)
    insertAtBottom(S, temp)


if __name__ == '__main__':
    st = [1, 2, 18, 8, 7, 10]
    stack(st)
    print(st)
    # print(reverseStack(stack))

