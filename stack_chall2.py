class Stack:
    def __init__(self):
        self.nums = []
    
    def is_empty(self):
        return self.nums == []
    
    def push(self, num):
        self.nums.append(num)
    
    def pop(self):
        return self.nums.pop()
    
    def peek(self):
        pos = len(self.nums) - 1
        return self.nums[pos]
    
    def size(self):
        return len(self.nums)

data = [1, 2, 3, 4, 5]
data1 = []

stack = Stack()

for item in data:
    stack.push(item)

for i in range(len(stack.nums)):
    data1.append(stack.pop())

print(data1)