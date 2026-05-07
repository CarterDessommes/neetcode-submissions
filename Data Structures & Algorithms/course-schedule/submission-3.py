class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = defaultdict(list)
        indegree = [0] * numCourses

        for prereq in prerequisites:
            indegree[prereq[1]] += 1
            adj_list[prereq[0]].append(prereq[1])
        
        q = deque()

        for course in range(len(indegree)):
            if indegree[course] == 0:
                q.append(course)

        order = []
        while q:
            cur = q.popleft()
            order.append(cur)

            for course in adj_list[cur]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        
        return len(order) == numCourses



        
        


        