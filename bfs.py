class Node:
  def __init__(self, name):
    self.name = name
    self.adjacency_list = []
    self.visited = False

def breadth_first_search(start_node):
  # FIFO: First item we insert will be taken out first
  queue = [start_node]

  # We keep iterating (considering the neighbour) until the queue is empty
  while queue:

    # Remove and return the first item we have inserted in queue
    actual_node = queue.pop(0)
    actual_node.visited = True
    print(actual_node.name)

    # Let's consider the neighbour one by one
    for n in actual_node.adjacency_list:
      if not n.visited:
        queue.append(n)

if __name__ == '__main__':
  # We create the nodes or vertices
  node1 = Node('A')
  node2 = Node('B')
  node3 = Node('C')
  node4 = Node('D')
  node5 = Node('E')

  # We have to handle the neighbour

  node1.adjacency_list.append(node2)
  node1.adjacency_list.append(node3)
  node2.adjacency_list.append(node4)
  node4.adjacency_list.append(node5)

  # Run BFS algorithm

  breadth_first_search(node1)
