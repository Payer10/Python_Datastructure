class Stack:
    def __init__(self):
        self.items = []
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        if self.items == []:
            return True
        return False
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    while not s.is_empty():
        a = s.pop()
        print(a)
        