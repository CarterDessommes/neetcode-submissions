class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        

        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        
        
        def dfs(cur, goal, val, visited):
            if cur == goal:
                return val
            
            visited.add(cur)
            
            for adj, w in graph[cur]:
                if adj not in visited:
                    result = dfs(adj, goal, val * w, visited)

                    if result != -1:
                        return result
            
            return -1
            

        
        sol = []
        for a, b in queries:
            if a not in graph or b not in graph:
                sol.append(-1)
            else: 
                sol.append(dfs(a, b, 1, set()))

        return sol






        