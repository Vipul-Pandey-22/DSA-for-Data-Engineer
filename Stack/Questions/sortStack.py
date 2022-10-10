def sortStack(s, ele):
    if not s:
        s.append(ele)
        return

    top = s[-1]
    if ele > top:
        s.append(ele)
        return

    s.pop()

    sortStack(s, ele)
    s.append(top)


def getSortedStack(s):
    if not s:
        return

    temp = s[-1]
    s.pop()
    # sortStack(s, temp)
    getSortedStack(s)
    sortStack(s, temp)


if __name__ == '__main__':
    st = [11, 2, 32, 3, 41]
    getSortedStack(st)
    print(st)
