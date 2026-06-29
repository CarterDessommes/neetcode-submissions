# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        # recursively just do a post order traveral of the tree
        # finding the height of each nodes subrtrees, with
        # the answer just being the max sum we find through this traversal
        # importantly, we want to return the heights which we are using
        # to calculate our result which is a global. making it 
        # slightly non trivial.
        def dfs(cur):
            if not cur:
                return 0
            
            left = dfs(cur.left)
            right = dfs(cur.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.res

        