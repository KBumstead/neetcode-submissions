# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        arr = []
        if root is None:
            return arr

        que = deque([root])
        count = 0

        while que:
            count = len(que)
            for i in range(count):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                
                if i == count - 1:
                    arr.append(node.val)

            
            count = 0

        return arr
        
