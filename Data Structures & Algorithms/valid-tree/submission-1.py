class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree is connectyed acylic graph? 

        if len(edges) != n-1:
            return False
        
        q = deque()
        visited = set()

        e = defaultdict(list)

        for edge in edges:
            e[edge[0]].append(edge[1])
            e[edge[1]].append(edge[0])

        q.append(0)
        visited.add(0)

        while q:
            val = q.popleft()

            for connection in e[val]:
                if connection not in visited:
                    visited.add(connection)
                    q.append(connection)

        
        if len(visited) != n:
            return False
        
        return True

        