"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        clones = {None: None}
        cur = head
        while cur is not None:
            clone = Node(cur.val, None, None)
            clones[cur] = clone
            cur = cur.next
        
        cur2 = head
        while cur2 is not None:
            clone = clones[cur2]
            clone.next = clones[cur2.next]
            clone.random = clones[cur2.random]
            cur2 = cur2.next
        
        return clones[head]
            






     
        