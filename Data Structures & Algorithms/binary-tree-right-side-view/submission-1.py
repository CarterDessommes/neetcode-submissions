# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:


        result = []
        q = deque()
        q.append(root)
        while q:
            qLen = len(q)
            layer = []
            for i in range(qLen):
                cur = q.popleft()
                if cur:
                    layer.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if layer:
                result.append(layer[-1])
        
        return result

        