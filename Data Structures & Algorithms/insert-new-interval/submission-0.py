class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        start, end = newInterval[0], newInterval[1]


        i = 0
        while i < len(intervals) and intervals[i][1] < start:
            i += 1

        sol = intervals[:i]
        
        while i < len(intervals) and intervals[i][0] <= end:
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            i += 1
        
        sol.append([start, end])
        sol.extend(intervals[i:])
        return sol




        