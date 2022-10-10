# Stack With No Size
class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        values = self.stack.reverse()
        values = [str(x) for x in self.stack]
        return '\n'.join(values)

    def isEmpty(self):
        if len(self.stack) == 0:
            return "Array is Empty"
        return "stack is not empty"

    def push(self, data):
        self.stack.append(data)
        return

    def pop(self):
        self.stack.pop()
        return

    def peek(self):
        return self.stack[-1]


st = Stack()
st.push(110)
st.push(120)
st.push(150)
st.push(160)

print(st.peek())
print(st.isEmpty())
print(st)




