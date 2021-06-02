class Node(object):
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class Bst(object):
  def __init__(self):
    self.root = None

  def insert(self, data):
    if self.root is None:
      self.root = Node(data)
    else:
      self.insert_node(data, self.root)

  def insert_node(self, data, node):
    if data < node.data:
      if node.left is None:
        node.left = Node(data)
      else:
        self.insert_node(data, node.left)
    else:
      if node.right is None:
        node.right = Node(data)
      else:
        self.insert_node(data, node.right)

  def get_min_value(self):
    if self.root:
      return self.get_min(self.root)

  def get_min(self, node):
    if node.left:
      return self.get_min(node.left)

    return node.data

  def get_max_value(self):
    if self.root:
      return self.get_max(self.root)

  def get_max(self, node):
    if node.right:
      return self.get_max(node.right)

    return node.data

  def traverse(self):
    if self.root:
      arr = []
      arr = self.traverse_inorder(self.root, arr)
      return arr

  def traverse_inorder(self, node, arr):
    if node.left:
      self.traverse_inorder(node.left, arr)

    arr.append(node.data)
    # print("%s "% node.data)

    if node.right:
      self.traverse_inorder(node.right, arr)

    return arr

  def get_node(self, data):
    if self.root:
      return self.find_node(data, self.root)
    

  def find_node(self, data, node):
    if node is not None and data == node.data:
      return node

    if data < node.data:
      if node.left is not None:
        return self.find_node(data, node.left)
    else:
      if node.right is not None:
        return self.find_node(data, node.right)

  def remove(self, data):
    if self.root:
      self.root = self.remove_node(data, self.root)

  def remove_node(self, data, node):
    if not node:
      return node

    if data < node.data:
      node.left = self.remove_node(data, node.left)
    elif data > node.data:
      node.right = self.remove_node(data, node.right)
    else:
      if not node.left and not node.right:
        # print("Removing node with no left and right childs")
        del node
        return None
      if node.left is None:
        temp_node = node.right
        del node
        return temp_node
      if node.right is None:
        temp_node = node.left
        del node
        return temp_node

      temp_node = self.get_predecessor(node.left)
      node.data = temp_node.data
      node.left =  self.remove_node(temp_node.data, node.left)
    return node

  def get_predecessor(self, node):
    if node.right:
      return self.get_predecessor(node.right)

    return node


bst = Bst()
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(9)
bst.insert(6)

# bst.traverse()
print(bst.traverse())
# bst.remove(5)
# bst.traverse()
# bst.get_node(5)
# print("Min Value is %s "% bst.get_min_value())
# print("Max Value is %s "% bst.get_max_value())
# print("Find 6 %s "% bst.get_node(5))
