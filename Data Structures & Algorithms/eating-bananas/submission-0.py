class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        c = (l + r) // 2
        while l < r:
            #print(f"{l} and {r}")
            time = 0
            
            for j in range(len(piles)):
                time += math.ceil(piles[j] / c) 

            if time <= h:
                r = c
            else:
                l = c + 1

            c = (l + r) // 2
        
        return l

            
           
        
            
            
            

                

