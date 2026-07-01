# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode: 
        # Idea is that because its a BST, as soon as both nodes aren't on the 
        # same side of the tree we know that this must be the LCA.
        # def dfs(cur):
        #     if cur.val > p.val and cur.val > q.val:
        #         return dfs(cur.left)
        #     elif cur.val < p.val and cur.val < q.val:
        #         return dfs(cur.right)
        #     else:
        #         return cur
            
        # lca = dfs(root)

        # return lca
        
        # o(1) space solution jsut iterates
        cur = root
        while cur:
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            else:
                return cur
