class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = [0] * numCourses

        for dst, src in prerequisites:
            adj_list[src].append(dst)
            indegree[dst] += 1
        
        no_pres = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                no_pres.append(i)
        
        order = []
        while no_pres:
            cur = no_pres.pop()
            order.append(cur)
            for dst in adj_list[cur]:
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    no_pres.append(dst)
        
        return order if len(order) == numCourses else []
            
            
            



