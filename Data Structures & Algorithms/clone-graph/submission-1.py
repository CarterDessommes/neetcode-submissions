"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        
        # need this to prevent loops,
        # track old node to new clone
        clones = {}

        def dfs(node):
            if node in clones:
                # this prevents loops
                return clones[node]
            
            # make a clone
            clone = Node()
            clone.val = node.val
            # remember it
            clones[node] = clone

            # add its neighbors
            for n in node.neighbors: 
                clone.neighbors.append(dfs(n))
            
            # return the clone
            return clone
        
        return dfs(node)