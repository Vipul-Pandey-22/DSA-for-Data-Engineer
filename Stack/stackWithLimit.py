class Stack:
    def __init__(self, limit):
        self.limit = limit
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        return False

    def isFull(self):
        if len(self.list) == self.limit:
            return True
        return False

    def push(self, data):
        if self.isFull():
            print("Overflow Condition. Stack is full")
            return
        else:
            self.list.append(data)
            print("Element inserted successfully")
            return

    def pop(self):
        if self.isEmpty():
            print("Underflow Condition. Stack is already empty")
            return
        else:
            self.list.pop()
            print("Value popped from stack")
            return

    def top(self):
        return self.list[-1]


st = Stack(10)
st.push(10)
st.push(12)
st.push(14)
print(st)

