class Stack:

    def __init__(self):
        self.chars = []
    
    def push(self, char):
        self.chars.append(char)
    
    def is_empty(self):
        return self.chars == []
    
    def pop(self):
        return self.chars.pop()
    
    def peek(self):
        pos = len(self.chars) - 1
        return self.chars[pos]
    
    def size(self):
        return len(self.chars)

a_stack = Stack()

for i in "yesterday":
    a_stack.push(i)

outtext = ""

while a_stack.size():
    outtext += a_stack.pop()

print(outtext)