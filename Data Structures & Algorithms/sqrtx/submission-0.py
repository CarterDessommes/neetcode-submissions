class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        i = 2
        j = x // 2
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
        
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
#.         j  
#.      m  i