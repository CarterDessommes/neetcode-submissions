class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        adj = [[] for _ in range(n + 1)]
        # build graph once
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        cycle = set()
        start = -1

        def dfs(cur, parent):
            nonlocal start
            # if we have seen it beofre we must
            # be starting the cycle
            if cur in visited:
                start = cur
                return True

            # add current to visited
            visited.add(cur)
            for n in adj[cur]:
                if n == parent:
                    continue
                
                # unravel the cycle 
                if dfs(n, cur):
                    if start != -1:
                        cycle.add(cur)
                    
                    # if we see the start again 
                    # we know for the rest of the 
                    # unraveling we shouldnt add to cycle
                    if cur == start:
                        start = -1
                    return True

            return False
                


        
        dfs(1, -1)
        # find the cycle edge that appears last we can remove
        for a, b in reversed(edges):
            if a in cycle and b in cycle:
                return [a, b]
            
        return []
