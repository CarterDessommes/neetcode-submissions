# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return self.recursion(root)
        
    
    def recursion(self, cur: Optional[TreeNode]) -> int:
        if not cur:
            return 0


        left = self.recursion(cur.left) + 1
        right = self.recursion(cur.right) + 1

        best = max(left, right)

        return best


