def solve(S, size, data):
    if size == 0:
        S.append(data)
        return

    temp = S[-1]
    S.pop()
    solve(S, size-1, data)
    S.append(temp)


def insertAtBottom(S, size, data):
    solve(S, size, data)


if __name__ == '__main__':
    stack = [4, 5, 1, 4]
    val = int(input())
    insertAtBottom(stack, len(stack), val)
    print(stack)
