def reverseString(string):
    from queue import LifoQueue
    stack = LifoQueue(maxsize=len(string))
    ans = ""
    for i in string:
        stack.put_nowait(i)

    while not stack.empty():
        temp = stack.get_nowait()
        ans += temp

    return ans


takeInputAsString = input()
print(reverseString(takeInputAsString))
