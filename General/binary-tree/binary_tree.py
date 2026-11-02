class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def inorder(node):
        if node:
            inorder(node.left)
            print(node.val)
            inorder(node.right)
