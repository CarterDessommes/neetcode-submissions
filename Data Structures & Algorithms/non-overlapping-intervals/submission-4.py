class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: (x[1], x[0]))

        if not intervals:
            return 0

        count = 0
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            print(f"{i}")
            cur_start = intervals[i][0]
            print(f"comparing {cur_start} < {prev_end}")
            if cur_start < prev_end:
                print(f"incrementing {count}")
                count += 1
            else:
                print(f"compairson is false, moving end")
                prev_end = intervals[i][1]
        
        return count
            






        

# [1, 6]
# [1, 2]
# [2, 7]
