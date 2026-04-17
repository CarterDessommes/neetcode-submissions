class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        adj_list = defaultdict(list)
        indegree = [0] * (n + 1)
        for src, dst in trust:
            adj_list[src].append(dst)
            indegree[dst] += 1
        
        ppl_who_everyone_trust = [] 
        for i in range(1, n + 1):
            if indegree[i] == n - 1:
                ppl_who_everyone_trust.append(i)
        
        
        for person in ppl_who_everyone_trust:
            if len(adj_list[person]) == 0:
                return person
        
        return -1

    #n=2
    # trust=[[1,2]]
    # indegree = [0, 0, 1]
    # adj = {1: [2], 2: []}


        