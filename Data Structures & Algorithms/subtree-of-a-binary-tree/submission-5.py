# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if the subRoot is not there, we know its true because its empty
        if not subRoot:
            return True
        
        # otherwise we know the answer is false
        if not root:
            return False

        # function to ensure trees are the same
        def isSameTree(root, subRoot):
            if not subRoot and not root:
                return True

            if not subRoot or not root:
                return False

            if root.val != subRoot.val:
                return False
            
            return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)

        # check the root node
        if isSameTree(root, subRoot):
            return True

        # otherwise try every node in the tree
        return (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot))

        
      