# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # just make a map that maps values to their inorder indexes
        # so reduce lookups to cost just O(n) one time at the start
        index_map = {val: idx for idx, val in enumerate(inorder)}

        # for some reason this solution is a bit tricky 
        # for me to wrap my head around
        self.preorder_index = 0
        def dfs(l, r):
            # base case, if l > r then there are no 
            # values left in this inorder section so we 
            # can jsut return
            # basically we hit this case when we call dfs
            # on a node with no children in its left or right tree
            if l > r:
                return None
            
            val = preorder[self.preorder_index]
            mid = index_map[val]
            self.preorder_index += 1
            root = TreeNode(val)
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        
        return dfs(0, len(inorder) - 1)
        