class Node():
    def __init__(self, data):
        self.data = data;
        self.next = None;

class Stack():
    def __init__(self):
        self.head = None;
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def push(self, data):
        self.size = self.size + 1
        if self.head is None:
            self.head = Node(data)
            self.head.next = None
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.head is None:
            return None

        self.size = self.size - 1

        currentNode = self.head

        self.head = currentNode.next

        return currentNode.data

    def peek(self):
        if self.head is None:
            return None

        return self.head.data

    def stackSize(self):
        return self.size

    def traverseStack(self):
        actualNode = self.head;

        while actualNode is not None:
            print("%d "% actualNode.data);
            actualNode = actualNode.next;



stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(50)
stack.traverseStack()
print(stack.stackSize())

print("Popped: ", stack.pop())

print("Peeked: ", stack.peek())
print(stack.stackSize())
stack.traverseStack()
