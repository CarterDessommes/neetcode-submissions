# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:



        def dfs(cur, lower, upper):
            if not cur:
                return True
            
            if cur.val <= lower or cur.val >= upper:
                return False

            result = dfs(cur.right, cur.val, upper) and dfs(cur.left, lower, cur.val)
            return result
        

        return dfs(root, float('-inf'), float('inf'))
