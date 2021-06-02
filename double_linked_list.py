class Node(object):
    def __init__(self, data):
        self.data = data;
        self.nextNode = None;
        self.previousNode = None;

class DoubleLinkedList(object):
    def __init__(self):
        self.head = None;
        self.size = 0

    def insertStart(self, data):
        self.size = self.size + 1;
        newNode = Node(data);

        if self.head is None:
            self.head = newNode;
        else:
            currentNode = self.head;
            newNode.nextNode = currentNode;
            currentNode.previousNode = newNode;
            self.head = newNode;

    def insertEnd(self, data):
        self.size = self.size + 1;
        newNode = Node(data);
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode;
        newNode.previousNode = actualNode

    def remove(self, data):
        if self.head is None:
            return

        self.zise = self.size - 1;
        currentNode = self.head
        while currentNode.data != data:
            currentNode = currentNode.nextNode

        if currentNode.previousNode is None:
            self.head = currentNode.nextNode
            currentNode.nextNode.previousNode = None;
        elif currentNode.nextNode is None:
            currentNode.previousNode.nextNode = None;
        else:
            currentNode.previousNode.nextNode = currentNode.nextNode;
            currentNode.nextNode.previousNode = currentNode.previousNode


    def traverseNode(self):
        while self.head is not None:
            print("%d "% self.head.data);
            self.head = self.head.nextNode;


doubleLinkedList = DoubleLinkedList();
doubleLinkedList.traverseNode();

doubleLinkedList.insertStart(3);
doubleLinkedList.insertStart(39);
doubleLinkedList.insertStart(7);
doubleLinkedList.insertStart(79);
doubleLinkedList.insertEnd(89);
doubleLinkedList.remove(7);

doubleLinkedList.traverseNode();


# 
# arr = [1,2,3,4,5,6,7,8]
# n = len(arr)
# print(n)
# for x in range(n-1,2,-1):
#   print(arr[x])
#
#
#
# arr = [1,0,2,3,0,4,5,0]
#
#
# n=len(arr)
# count_zero = len([x for x in arr if x==0])
#
# for i in range (n-1,-1,-1):
#     if arr[i]==0:
#         count_zero-=1
#
#     index=i+count_zero
#     if index<n:
#         arr[index]=arr[i]
#
# i=0
# while(i<n):
#     if arr[i]==0 and i+1<n:
#         arr[i+1]=0
#         i+=2
#     else:
#         i+=1
#
# i = 0
# while i>=n:
#     if arr[i] == 0:
#         for j in range(n-1,i+2,-1):
#             arr[j] = arr[j-1];
#
#         if i+1 < n:
#             arr[i+1] = 0;
#         i = i+2;
#
#
# for i in range(n):
#     if arr[i] == 0:
#         for j in range(n-2,i+1,-1):
#             arr[j+1] = arr[j];
#
#         if i+1 < n:
#             arr[i+1] = 0;
#         i = i+2;
