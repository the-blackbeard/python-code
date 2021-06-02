from collections import defaultdict
class Graph:
  def __init__(self, vertices):
    self.graph = defaultdict(list)
    self.v = vertices

  #Function to append edge
  def add_edge(self, u, v):
    self.graph[u].append(v)

  def topologicalSortUtil(self, vertex, visited, stack):
    visited[vertex] = True

    for i in self.graph[vertex]:
      if visited[i] == False:
        self.topologicalSortUtil(i, visited, stack)

    stack.append(vertex)

  # The function to do Topological Sort. It uses recursive 
  # topologicalSortUtil()
  def topological_sort(self):
    visited = [False] * self.v
    stack = []

    for i in range(self.v):
      if visited[i] == False:
        self.topologicalSortUtil(i, visited, stack)

    return stack[::-1]


g = Graph(6) 
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print "Following is a Topological Sort of the given graph"

print(g.topological_sort())