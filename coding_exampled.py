class newNode:  
  
  # Constructor to create a new node  
  def __init__(self, data):  
    self.key = data  
    self.left = None
    self.right = None

# To insert a new node in BST 
def insert(node, key):
	if node is None:
		return newNode(key)

	if key < node.key:
		node.left = insert(node.left, key)
	elif key > node.key:
		node.right = insert(node.right, key)

	return node

# function to find max value less then N Using DFS
# def findMaxforN(node, n):
# 	stack = [node]
# 	diff = [float('inf'), -1]

# 	while stack:
# 		curr_node = stack.pop()

# 		new_diff = n - curr_node.key

# 		if new_diff >= 0 and new_diff < diff[0]:
# 			diff = [new_diff, curr_node.key]

# 		if curr_node.key <= n:
# 			if curr_node.right:
# 				stack.append(curr_node.right)
# 		else:
# 			if curr_node.left:
# 				stack.append(curr_node.left)

	return diff[1]

# function to find max value less then N Using recursion
def findMaxforN(node, n):
	if node is None:
		return -1
	if node.key == n:
		return n
	elif node.key < n:
		k = findMaxforN(node.right, n)
		if k == -1:
			return node.key
		else:
			return k
	elif node.key > n:
		return findMaxforN(node.left, n)



# Driver code 
if __name__ == '__main__':
	N = 0

	# creating following BST 
	# 
	#			 5 
	#		 / \ 
	#		 2	 12 
	#	 / \ / \ 
	#	 1 3 9 21 
	#				 / \ 
	#			 19 25 

	root = None
	root = insert(root, 5)
	insert(root, 2)
	insert(root, 1)
	insert(root, 3)
	insert(root, 12)
	insert(root, 9)
	insert(root, 21)
	insert(root, 19)
	insert(root, 25)


	print(findMaxforN(root, N))