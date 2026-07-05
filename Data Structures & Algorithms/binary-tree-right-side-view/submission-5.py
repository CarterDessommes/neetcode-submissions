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
            # originally did this by building the list
            # of the layer and just adding the 
            # last elem but you can also just 
            # do this which is more space efficinet
            rightNode = None
            for i in range(qLen):
                cur = q.popleft()
                if cur:
                    rightNode = cur
                    q.append(cur.left)
                    q.append(cur.right)
            if rightNode:
                result.append(rightNode.val)
        
        return result

        