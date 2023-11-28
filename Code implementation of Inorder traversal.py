class Node:
    def __init__(self,key):
         self.left = None
         self.right = None
         self.val = key
def PrintInorder(root):
    if root:
        PrintInorder(root.left)
        print(root.val,end=" ")
        PrintInorder(root.right)
if __name__ =="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Inorder traverse of binary tree is :")
    PrintInorder(root)
