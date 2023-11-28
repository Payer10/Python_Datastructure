class Queue:
    def __init__(self,size):
        self.items=[0]*size
        self.max_size=size
        self.head=0
        self.tail=0
        self.size=0
    def enqueue(self,item):
        if self.is_ful():
            print('Queue is ful')
            return
        print('Interesting',item)
        self.items[self.tail]=item
        self.tail=(self.tail+1)%self.max_size
        self.size+=1
    def dequeue(self):
        item=self.items[self.head]
        self.head=(self.head+1)%self.max_size
        self.size-=1
        return item
        
    def is_ful(self):
        if self.size==self.max_size:
            return True
        return False
    def is_empty(self):
        if self.size==0:
            return True
        return False
if __name__ == "__main__":
    q=Queue(3)
    q.enqueue('payer')
    q.enqueue('ahmed')
    q.enqueue('opu')
    q.enqueue('mohammad')
    while not q.is_empty():
        person=q.dequeue()
        print(person)

    

    
