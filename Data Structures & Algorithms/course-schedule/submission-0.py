class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        no_pres = deque()
        num_taken = 0
        for p in prerequisites:
            c = p[0]
            pre = p[1]
            adj_list[c].append(pre)

        for i in range(numCourses):
            if len(adj_list[i]) == 0:
                no_pres.append(i)
        
        while no_pres:
            cur = no_pres.popleft()
            num_taken += 1
            for key in adj_list:
                if cur in adj_list[key]:
                    adj_list[key].remove(cur)
                    if len(adj_list[key]) == 0:
                        no_pres.append(key)
        
        return num_taken == numCourses

        

# [0,1]
# adj list = {0: [1], 1: []}
# no_pres = []
# cur = 1
        