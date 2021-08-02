class Node:
  def __init__(self, name):
    self.name = name
    self.adjacency_list = []
    self.visited = False


def depth_first_search(start_node):

  # We need LIFO structure
  stack = [start_node]

  while stack:
    actual_node = stack.pop()
    actual_node.visited = True

    print(actual_node.name)

    for n in actual_node.adjacency_list:
      if not n.visited:
        stack.append(n)

