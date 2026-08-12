class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        adj = [[] for _ in range(n + 1)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        cycle = set()
        start = -1

        def dfs(cur, parent):
            nonlocal start

            if cur in visited:
                start = cur
                return True

            visited.add(cur)
            for n in adj[cur]:
                if n == parent:
                    continue
                
                if dfs(n, cur):
                    if start != -1:
                        cycle.add(cur)
                    if cur == start:
                        start = -1
                    return True
            return False
                


        
        dfs(1, -1)

        for a, b in reversed(edges):
            if a in cycle and b in cycle:
                return [a, b]
            
        return []
