class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
def PrintPreorder(root):
    if root:
        print(root.val,end=" ")
        PrintPreorder(root.left)
        PrintPreorder(root.right)
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Preorder traverse of binary tree is :")
    PrintPreorder(root)
