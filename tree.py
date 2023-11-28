class Bainary_search:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Bainary_search(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Bainary_search(data)

    def in_order_traverse(self):
        element = []
        #visit left subtree
        if self.left:
            element += self.left.in_order_traverse()
        element.append(self.data)
        #visit right subtree
        if self.right:
            element += self.right.in_order_traverse()       
        return element

    def search(self,val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
               return self.left.search(val)
            else:
                return False
        else:
            if self.right:
               return self.right.search(val)
            else:
                return False

def build_tree(element):
    print('the build tree:',element)
    root = Bainary_search(element[0])
    
    for i in range(1,len(element)):
        root.add_child(element[i])
    return root

if __name__ == "__main__":
    number = [5,1,2,7,8,3,9,4,10]
    root = build_tree(number)
    print(root.in_order_traverse( ))

