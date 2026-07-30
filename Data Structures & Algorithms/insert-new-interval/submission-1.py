class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        start, end = newInterval[0], newInterval[1]
        
        # loop forward till we find our first conflicting time
        # where the one to insert starts before
        i = 0
        while i < len(intervals) and intervals[i][1] < start:
            i += 1

        # seed our solution array
        sol = intervals[:i]
        
        # while the current interval starts before our one to
        # insert ends
        while i < len(intervals) and intervals[i][0] <= end:
            # this min max handles all cases of overlap
            # just choose biggest window
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            i += 1
        
        sol.append([start, end])
        # extend here to get the elements individually
        sol.extend(intervals[i:])
        return sol




        