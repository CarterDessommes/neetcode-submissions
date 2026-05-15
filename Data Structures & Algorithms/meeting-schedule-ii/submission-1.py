"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        key_times = []

        for interval in intervals:
            s = interval.start
            e = interval.end
            key_times.append((s, 1))
            key_times.append((e, -1))


        key_times.sort()

        m = 0
        s = 0
        for time, increment in key_times:
            s += increment
            m = max(m, s)
        
        return m



 
        