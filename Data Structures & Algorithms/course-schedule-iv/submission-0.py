class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = defaultdict(list)
        
        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(cur, goal, visited):
            if cur == goal:
                return True
            
            visited.add(cur)

            for adj in graph[cur]:
                if adj not in visited:
                    if dfs(adj, goal, visited):
                        return True
            
            return False

        
        sol = []
        for a, b in queries:
            sol.append(dfs(a, b, set()))

        return sol
