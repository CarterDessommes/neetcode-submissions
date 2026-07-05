# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0
            
            res = 0
            # if we have seen no larger number
            # change res to be one to increase
            # the count and update our maxVal
            if node.val >= maxVal:
                res += 1
                maxVal = node.val

            # recurse on the left and right kid
            # doing dfs sharing the maxVal seen
            # so far addind ot the result
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        
        return dfs(root, root.val)