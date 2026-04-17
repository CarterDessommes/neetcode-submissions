class Solution:
    def mySqrt(self, x: int) -> int:
     
        i = 0
        j = x 
        while i <= j:
            mid = (j - i) // 2 + i
            square = mid * mid
            if square < x:
                i = mid + 1
            elif square > x:
                j = mid - 1
            else:
                return mid
        return j
        
