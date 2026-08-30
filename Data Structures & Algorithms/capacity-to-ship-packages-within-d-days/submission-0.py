class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l < r:
            m = (l + r) // 2

            cur_days = 1
            s = 0

            for weight in weights:
                if s + weight > m:
                    cur_days += 1
                    s = 0
                
                s += weight
            
            if cur_days <= days:
                r = m
            else:
                l = m + 1

        return l            


