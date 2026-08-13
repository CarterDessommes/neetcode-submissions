class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        # pretty hyped i one shot this solution
        # not even like a grammer or code bug lol

        # apply the same idea as the evaluate dvision problem
        graph = defaultdict(list)
        
        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(cur, visited):            
            visited.add(cur)

            for adj in graph[cur]:
                if adj not in visited:
                    dfs(adj, visited)
                        
            
        # use a map to minimize repeated work,
        # so this way in the worst case we just run
        # dfs from every node onces, whereas otherwise
        # we could run from many nodes
        reachable = {}

        sol = []
        for a, b in queries:
            if a not in reachable:
                reachable[a] = set()
                dfs(a, reachable[a])
            
            sol.append(b in reachable[a])
            

        return sol
