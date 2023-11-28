class Node:
    def __init__ (self,data):
        self.data=data
        self.next=next
class linkedlist:
    def __init__(self):
        self.head=None
    def prepend(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
    def append(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        current_node=self.head
        while current_node.next:
            current_node=current_node.next
        current_node.next=node
        
q=linkedlist()
q.prepend(1)
q.prepend(2)
q.prepend(3)
q.append(4)
q.append(5)
print(q.head.data)
print(q.head.next.data)
print(q.head.next.next.data)
print(q.head.next.next.next.data)
print(q.head.next.next.next.next.data)
print(q.head.next.next.next.next.data)
