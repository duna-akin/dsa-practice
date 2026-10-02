# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        lHeight = self.height(root.left)
        rHeight = self.height(root.right)

        nDiam = lHeight + rHeight
        lDiam = self.diameterOfBinaryTree(root.left)
        rDiam = self.diameterOfBinaryTree(root.right)

        return max(nDiam, lDiam, rDiam)
    
    def height(self, node):
        if node is None:
            return 0
        
        return 1 + max(self.height(node.left), self.height(node.right))