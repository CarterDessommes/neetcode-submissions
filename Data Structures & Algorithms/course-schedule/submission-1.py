class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        
        
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj_list[src].append(dst)

        no_pres = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                no_pres.append(i)
        num_taken = 0
        while no_pres:
            num_taken += 1
            cur = no_pres.popleft()
            for c in adj_list[cur]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    no_pres.append(c)
        
        return num_taken == numCourses

        

# [0,1]
# adj list = {0: [1], 1: []}
# no_pres = []
# cur = 1
        