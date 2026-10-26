# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = 0

        def dfs(node):
            if node is None:
                return [0, False]
            
            nonlocal count

            left = dfs(node.left)

            if left[1]:
                return left

            count += 1

            if count == k:
                return [node.val, True]

            
            right = dfs(node.right)

            if right[1]:
                return right

            return [0, False]

        return dfs(root)[0]




        