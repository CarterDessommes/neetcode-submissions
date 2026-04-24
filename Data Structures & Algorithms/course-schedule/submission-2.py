class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] += 1
        
        q = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
        
        sol = []
        while q:
            cur = q.popleft()
            sol.append(cur)
            for adj in adj_list[cur]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)
                
                
        return len(sol) == numCourses
        

# [0,1]
# adj list = {0: [1], 1: []}
# no_pres = []
# cur = 1
        