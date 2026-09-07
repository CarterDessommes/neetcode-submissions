# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            # search left and update root
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # search right and update root
            root.right = self.deleteNode(root.right, key)
        else:
            # if we found it and it has no left kid (or no kids), just return its right
            if not root.left:
                return root.right

            # same logic on right
            elif not root.right:
                return root.left
            
            # otherwise it has two kids 
            else:
                repl = self.successor(root.right)
                root.val = repl.val
                root.right = self.deleteNode(root.right, repl.val)
            
        
        return root

            
            
    def successor(self, root):
        if not root.left:
            return root
        
        return self.successor(root.left)




