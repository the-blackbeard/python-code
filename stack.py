class Stack():
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def sizeStack(self):
        return len(self.stack)

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.sizeStack())
print("Popped: ", stack.pop())
print("Popped: ", stack.pop())
print(stack.sizeStack())
print("Peeked: ", stack.peek())
print(stack.sizeStack())




[
    [0,0,0,1],
    [0,1,0,0],
    [0,0,1,0],
    [1,0,0,0],
    [0,0,0,0]
]



houses_arr = []
cols = len(matrix)
rows = len(matrix[0])
counter = 0

for i in range(cols):
    for j in range(rows):
        if matrix[i][j] == 1:
            houses_arr.append(set(i,j))


for i in range(cols):
    for j in range(rows):
        is_counter = False
        for x in range(len(houses_arr)):
            dist = abs(houses_arr[x][0] - i) + abs(houses_arr[x][1] - j)
            if dist <= k:
                is_counter = True
        if is_counter:
            counter += 1

return counter



