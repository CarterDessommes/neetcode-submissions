# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        order = []
        
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            dfs(cur.right)
            temp = cur.right
            cur.right = cur.left
            cur.left = temp

        dfs(root)
        return root


        