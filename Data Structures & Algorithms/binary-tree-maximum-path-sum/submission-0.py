# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # for each node the max val is either
        # sum of left and right max and cur node
        # or left or right max plus cur node
        # at top level return the max of this 
        # value we find. if we are ever adding a 
        # negative, add a zero instead 

        res = root.val

        def dfs(node):
            nonlocal res
            # base case
            if node is None:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            both = node.val + left + right
            one = node.val + max(left, right)

            res = max(res, both, one)

            return node.val + max(left, right)

        dfs(root)
        return res
        