def heapify(arr, index):
	largest = index
	left = (index * 2) + 1
	right = (index * 2) + 2 

	if left < len(arr) and arr[left] > arr[largest]:
		largest = left

	if right < len(arr) and arr[right] > arr[largest]:
		largest = right

	if index != largest:
		arr[index], arr[largest] = arr[largest], arr[index]
		heapify(arr, largest)


def build_head(arr):
	size = len(arr)
	parent_nodes = (size//2) - 1

	for i in range(parent_nodes,-1,-1):

		heapify(arr, i)

def print_heap(arr): 
    print("Array representation of Heap is:"); 
  
    for i in range(len(arr)):
        print(arr[i])

if __name__ == '__main__':

	arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]

	build_head(arr)

	print_heap(arr)