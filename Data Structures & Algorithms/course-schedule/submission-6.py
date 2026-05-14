class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses

        adj = defaultdict(list)

        for prereq in prerequisites:
            a, b = prereq[0], prereq[1]
            indegree[a] += 1
            adj[b].append(a)
        
        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        order = []
        while q:
            cur = q.popleft()
            order.append(cur)

            for a in adj[cur]:
                indegree[a] -= 1
                if indegree[a] == 0:
                    q.append(a)
            
        return len(order) == numCourses






        
        


        