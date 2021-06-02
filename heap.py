#Max number of items that can be stored in a heap
CAPACITY = 10

class Heap(object):
    def __init__(self):
        #Create an array with as many slot as CAPACITY
        self.heap = [0]*CAPACITY;
        #To track the size
        self.heap_size = 0

    def insert(self, item):
        if CAPACITY == self.heap_size:
            return

        self.heap[self.heap_size] = item
        self.heap_size = self.heap_size + 1

        self.fix_up(self.heap_size-1)

    def fix_up(self, index):
        #To get the integer value we are using '//' instead of '/'
        parent_index = (index-1)//2

        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.swap(index, parent_index)
            self.fix_up(parent_index)

    def swap(self, index1, index2):
        self.heap[index2], self.heap[index1] = self.heap[index1], self.heap[index2]

    def get_max(self):
        return self.heap[0]

    def poll(self):
        max = self.get_max()

        self.swap(0, self.heap_size-1)
        self.heap_size = self.heap_size - 1

        self.fix_down(0)

        return max

    def fix_down(self, index):
        index_left = (index*2) + 1
        index_right = (index*2) + 2

        index_largest = index

        if index_left < self.heap_size and self.heap[index_left] > self.heap[index]:
            index_largest = index_left

        if index_right < self.heap_size and self.heap[index_right] > self.heap[index_largest]:
            index_largest = index_right

        if index != index_largest:
            self.swap(index, index_largest);
            self.fix_down(index_largest)

    def get_heap_size(self):
        return self.heap_size

    def heap_sort(self):
        size = self.heap_size

        for i in range(size):
            max = self.poll()
            print(max)


if __name__ == '__main__':
    heap = Heap()

    heap.insert(10)
    heap.insert(8)
    heap.insert(12)
    heap.insert(20)
    heap.insert(-1)
    heap.insert(0)
    heap.insert(1)
    heap.insert(321)

    # print(heap.poll())
    # print(heap.get_max())
    # print(heap.get_heap_size())

    heap.heap_sort()
