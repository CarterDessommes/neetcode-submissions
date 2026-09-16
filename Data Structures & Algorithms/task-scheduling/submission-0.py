class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks)

        vals = [cnt for cnt in counts.values()]
        vals.sort()

        # 
        num_slots = vals[-1] - 1

        # total number of idle slots needed
        idle = (num_slots) * n

        for val in vals[:-1]:
            idle -= min(val, num_slots)
        
        if idle > 0:
            return len(tasks) + idle

        return len(tasks)


        
