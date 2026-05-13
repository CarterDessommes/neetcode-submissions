"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0
        res = 0

        times = []
        for i in intervals:
            times.append((i.start, 1))
            times.append((i.end, -1))

        times.sort(key=lambda x: (x[0], x[1]))

        res = 0
        cur = 0
        for time in times:
            cur += time[1]
            res = max(res, cur)
        
        return res


 
        