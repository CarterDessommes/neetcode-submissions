# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []

        def dfs(cur):
            if not cur:
                return 
            dfs(cur.left)
            dfs(cur.right)
            order.append(cur.val)
        
        dfs(root)
        return order
        