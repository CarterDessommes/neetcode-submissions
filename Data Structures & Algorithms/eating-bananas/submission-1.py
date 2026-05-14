class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        
        while l < r:
            k = (l + r) // 2

            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            
            if time > h:
                l = k + 1
            # if we have a valid time
            else:
                r = k
        
        return l

            
            

                

