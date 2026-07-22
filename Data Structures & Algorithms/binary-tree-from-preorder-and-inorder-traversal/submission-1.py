# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # just make a map that maps values to their inorder indexes
        index_map = {val: idx for idx, val in enumerate(inorder)}

        self.preorder_index = 0

        def dfs(l, r):
            if l > r:
                return None
            
            root = TreeNode(preorder[self.preorder_index])
            self.preorder_index += 1
            # o(n) to find the location at each step in the recursion
            # so overall is o(n^2)
            mid = index_map[root.val]
            left_subtree = dfs(l, mid - 1)
            right_subtree = dfs(mid + 1, r)

            root.left = left_subtree
            root.right = right_subtree

            return root
        
        return dfs(0, len(preorder) - 1)

