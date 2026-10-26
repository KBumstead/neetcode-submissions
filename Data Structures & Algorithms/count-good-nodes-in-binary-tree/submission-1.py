# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        def dfs(root, maximum):
            if root is None:
                return 0
            res = 0

            if root.val >= maximum:
                maximum = root.val
                res = 1
            
            res += dfs(root.left, maximum)
            res += dfs(root.right, maximum)
            
            return res


            
        return dfs(root, root.val)
        