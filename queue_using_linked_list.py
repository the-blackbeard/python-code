class Node():
    def __init__(self, data):
        self.data = data;
        self.next = None;

class Queue():
    def __init__(self):
        self.head = None;
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def enqueue(self, data):
        self.size = self.size + 1
        if self.head is None:
            self.head = Node(data)
            self.head.next = None
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def dequeue(self):
        if self.head is None:
            return None

        self.size = self.size - 1
        currentNode = self.head
        previousNode = None

        while currentNode.next is not None:
            previousNode = currentNode
            currentNode = currentNode.next

        previousNode.next = None
        return currentNode.data


    def peek(self):
        if self.head is None:
            return None

        currentNode = self.head
        previousNode = None

        while currentNode.next is not None:
            previousNode = currentNode
            currentNode = currentNode.next

        return currentNode.data

    def queueSize(self):
        return self.size

    def traverseQueue(self):
        actualNode = self.head;

        while actualNode is not None:
            print("%d "% actualNode.data);
            actualNode = actualNode.next;


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.traverseQueue()
print(queue.queueSize())

print("Popped: ", queue.dequeue())

print("Peeked: ", queue.peek())
print(queue.queueSize())
queue.traverseQueue()
