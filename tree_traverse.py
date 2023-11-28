class Tree_node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def Preorder_traverse(node):
    if node:
        print(node.data)
        Preorder_traverse(node.left)
        Preorder_traverse(node.right)
def Postorder_traverse(node):
    if node:
        Postorder_traverse(node.left)
        Postorder_traverse(node.right)
        print(node.data)
def Inorder_traverse(node):
    if node:
        Inorder_traverse(node.left)
        print(node.data)
        Inorder_traverse(node.right)
if __name__ == "__main__":
    root = Tree_node(2)
    root.left = Tree_node(9)
    root.right = Tree_node(7)
    root.left.left = Tree_node(3)
    root.right.right = Tree_node(8)
    print('Preorder_traverse')
    Preorder_traverse(root)
    print('Postorder_traverse')
    Postorder_traverse(root)
    print('Inorder_traverse')
    Inorder_traverse(root)