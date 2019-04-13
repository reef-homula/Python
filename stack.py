class Stack:
    def __init__(self):
        # itemsを空白に
        self.items = []
    def is_empty(self):
        # returnでT/Fが返せる。比較演算子をそのまま使える
        return self.items == []
    def push(self, item):
        # pushはappendで管理できる
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        # 閲覧するだけのときに限り、位置をしていする変数をマイナスし、最新を表示する。
        last = len(self.items) - 1
        return self.items[last]
    def size(self):
        return len(self.items)

stack = Stack()
print(stack.is_empty())

stack.push(1)

print(stack.is_empty())

print(stack.pop())

print(stack.is_empty())

stack.push(9)

print(stack.peek())

print(stack.is_empty())

print(stack.size())