class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        q = deque()
        components = 0

        visited = set()

        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        while len(visited) < n:
            components += 1
            for i in range(n):
                if i not in visited:
                    q.append(i)
                    visited.add(i)
                    break

            while q:
                cur = q.popleft()
                for connection in adj[cur]:
                    if connection not in visited:
                        visited.add(connection)
                        q.append(connection)
        
        return components





        