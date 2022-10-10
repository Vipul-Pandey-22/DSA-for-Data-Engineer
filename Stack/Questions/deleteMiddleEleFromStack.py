def solve(S, count, size):
    # base case
    if count == size // 2:
        S.pop()
        return

    temp = S.pop()
    # Recursive call
    solve(S, count+1, size)
    S.append(temp)


def deleteMiddle(S, size):
    count = 0
    solve(S, count, size)


if __name__ == '__main__':
    stack = [1, 3, 4, 5, 2]
    deleteMiddle(stack, len(stack)-1)
    print(stack)

