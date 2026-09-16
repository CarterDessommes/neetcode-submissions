class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks)

        vals = [cnt for cnt in counts.values()]
        vals.sort()

        # 
        num_slots = vals[-1] - 1

        # total number of idle slots remaining
        idle = (num_slots) * n
        
        # for each value, remove it from the 
        for val in vals[:-1]:
            # remove the max amount of idle slots we can using this 
            # letter
            idle -= min(val, num_slots)
        
        if idle > 0:
            # number of tasks plus idle slots we couldnt fill
            return len(tasks) + idle

        # otherwise there is a way with no idling we can do it
        return len(tasks)


        
