class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = [0] * numCourses

        for dst, src in prerequisites:
            indegree[dst] += 1
            adj_list[src].append(dst)
        
        no_pres = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                no_pres.append(i)
        
        order = []
        while no_pres:
            cur = no_pres.popleft()
            order.append(cur)
            for c in adj_list[cur]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    no_pres.append(c)
        
        return order if len(order) == numCourses else []



