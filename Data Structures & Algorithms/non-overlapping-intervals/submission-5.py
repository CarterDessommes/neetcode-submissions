class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # sory by end times for greedy
        intervals.sort(key=lambda x: (x[1], x[0]))

        if not intervals:
            return 0

        count = 0
        prev_end = intervals[0][1]

        # use greedy to choose soonest ending task each 
        # time, which will guarantee we pick the smallest
        # number of ones to remove each time
        for i in range(1, len(intervals)):
            cur_start = intervals[i][0]
            # if there is a conflict
            # then we can increment the count
            if cur_start < prev_end:
                count += 1
            # otherwise move what we are comparing to
            # forward
            else:
                prev_end = intervals[i][1]
        
        return count
            






        

# [1, 6]
# [1, 2]
# [2, 7]
