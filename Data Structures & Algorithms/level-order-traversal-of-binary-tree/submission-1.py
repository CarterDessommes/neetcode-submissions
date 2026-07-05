# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []
        q = deque()
        q.append(root)
        while q:
            layer = []
            nxt = deque()
            while q:
                cur = q.popleft()
                if cur:
                    layer.append(cur.val)
                    nxt.append(cur.left)
                    nxt.append(cur.right)
            
            q = nxt
            if layer:
                result.append(layer)
        
        return result




        

