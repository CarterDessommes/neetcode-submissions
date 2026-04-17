class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        sorted_intervals = sorted(intervals)
        result = []

        # [1,3],[1,5],[6,7]

        # 0
        i = 0
        while i < len(sorted_intervals):
            start = sorted_intervals[i][0]
            finish = sorted_intervals[i][1]
            # start = 1, finish = 3

            cur = [start, finish]
            # cur = [1, 3]
            j = i + 1
            # j = 1
            while j < len(sorted_intervals):

                next_start = sorted_intervals[j][0]
                next_finish = sorted_intervals[j][1]
                #next_start = 6, next_finish = 7
                

                if finish >= next_start:
                    finish = max(finish, next_finish)
                    cur[1] = finish
                    # changes from [1, 3] -> [1, 5]
                    j += 1
                    # j = 2
                else: 
                    break
            result.append(cur)
            i = j

        return result
            

                



            

        