class Node(object):
    def __init__(self, data):
        self.data = data;
        self.height = 0;
        self.rightChild = None;
        self.leftChild = None;

class AVL(object):
    def __init__(self):
        self.root = None;

    def insert(self, data):
        self.root = self.insertNode(data, self.root);

    def insertNode(self, data, node):
        if not node:
            return Node(data);

        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild);
        else:
            node.rightChild = self.insertNode(data, node.rightChild);

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
        return self.settleViolation(data, node);

    def settleViolation(self, data, node):
        balance = self.calcBalance(node);

        # Case 1: left left heavy situation or doubly left heavy situation -->> Single right rotation
        if balance > 1 and data < node.leftChild.data:
            print("This is left left heavy situation")
            return self.rotateRight(node);

        # Case 2: right right heavy situation or doubly right heavy situation -->> Single left rotation
        if balance < -1 and data > node.rightChild.data:
            print("This is right right heavy situation")
            return self.rotateLeft(node);

        # Case 3: left heavy but data is greater than node's left child data
        if balance > 1 and data > node.leftChild.data:
            print("Left right heavy situation")
            node.leftChild = self.rotateLeft(node.leftChild);
            return self.rotateRight(node)

        # Case 4: right heavy but data is smaller than node's right child data
        if balance < -1 and data < node.rightChild.data:
            print("Right left heavy situation")
            node.rightChild = self.rotateRight(node.rightChild);
            return self.rotateLeft(node);

        return node;

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        print("%s "% node.data)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)

    def calcHeight(self, node):
        if not node:
            return -1

        return node.height


    # If this method return > 1 then it is a left heavy tree ---> we have to make right rotation
    # If this method return < -1 then it is a right heavy tree ---> we have to make left rotation
    def calcBalance(self, node):
        if not node:
            return 0

        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)

    def rotateRight(self, node):
        print("Rotate to the right on node", node.data);

        tempLeftChild = node.leftChild;
        t = tempLeftChild.rightChild;

        tempLeftChild.rightChild = node;
        node.leftChild = t;

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1;

        return tempLeftChild;

    def rotateLeft(self, node):
        print("Rotate to the left on node", node.data);

        tempRightChild = node.rightChild;
        t = tempRightChild.leftChild;

        tempRightChild.leftChild = node;
        node.rightChild = t;

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;
        tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild)) + 1;

        return tempRightChild;

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                print("Removing node with no left and right childs")
                del node
                return None

            if not node.leftChild:
                print("Removing node with no left child")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print("Removing node with no right child")
                tempNode = node.leftChild
                del node
                return tempNode

            print("Removing with both childs")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        if not node:
            return node;

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1;

        balance = self.calcBalance(node);

        #doubly left heavy situation
        if balance > 1 and self.calcBalance(node) >= 0:
            print("Doubly left heavy situation")
            return self.rotateRight(node);

        #Left right heavy situation
        if balance > 1 and self.calcBalance(node) < 0:
            print("Left right heavy situation")
            node.leftChild=  self.rotateLeft(node.leftChild);
            return self.rotateRight(node);

        #doubly right heavy situation
        if balance < -1 and self.calcBalance(node) <= 0:
            print("Doubly right heavy situation")
            return self.rotateRight(node);

        #Left right heavy situation
        if balance < -1 and self.calcBalance(node) > 0:
            print("Right left heavy situation")
            node.rightChild=  self.rotateRight(node.rightChild);
            return self.rotateLeft(node);

        return node

    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node


avl = AVL();
avl.insert(10);
avl.insert(20);
avl.insert(5);
avl.insert(4);
avl.insert(15);


avl.remove(15);
avl.remove(20);

avl.traverse();


string_lenght = len(s)
letter_hash = {}

for i in range(string_lenght):
  if letter_hash.has_key(s[i]):
    letter_hash[s[i]] = letter_hash[s[i]]+1
  else:
    letter_hash[s[i]] = 1






