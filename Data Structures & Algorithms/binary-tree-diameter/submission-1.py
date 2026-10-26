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
        
        maxLeft = self.maxHeight(root.left)
        maxRight = self.maxHeight(root.right)
        diameter = maxLeft + maxRight

        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(diameter, sub)




    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        return 1 + max(self.maxHeight(root.right), self.maxHeight(root.left))
    