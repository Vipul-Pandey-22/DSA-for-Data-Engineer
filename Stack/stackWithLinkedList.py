class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.data) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.LinkedList.head
        self.LinkedList.head = newNode

    def pop(self):
        if self.isEmpty():
            return "there is any element"
        else:
            nodeValue = self.LinkedList.head.data
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    def peek(self):
        if self.isEmpty():
            return "there is no any element"
        return self.LinkedList.head.data

    def delete(self):
        self.LinkedList.head = None


customStack = Stack()
print(customStack.isEmpty())
customStack.push(10)
customStack.push(1)
customStack.push(0)
customStack.push(19)
print(customStack)
print("----------------------------------")
print(customStack)
print(customStack.peek())
