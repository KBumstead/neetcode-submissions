# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        

        def dfs(node, minVal, maxVal):
            if node is None:
                return True
            
            bInRange = node.val > minVal and node.val < maxVal

            left = dfs(node.left, minVal, node.val)
            right = dfs(node.right, node.val, maxVal)

            return left and right and bInRange

        return dfs(root, float('-inf'), float('inf'))
