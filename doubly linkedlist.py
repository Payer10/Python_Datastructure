class Node:
    def __init__(self,data,prev,next):
        self.data=data
        self.prev=prev
        self.next=next
class Doublylinkedlist:
    def __init__(self):
        self.head=Node()
        nodes=[]
        current_node=self.head
        while current_node:
            nodes.append(current_node)
            current_node=current_node.next
    def append(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        current_node=self.head
        while current_node.next:
            current_node=current_node.next
        current_node.next=node
        node.prev=current_node
    def prepend(self,data):
        frist_node=self.head
        node=(data,None,frist_node)
        self.head=node
        if frist_node:
            frist_node.next=node







        
