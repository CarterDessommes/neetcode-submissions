class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        maxL = [0] * n
        maxR = [0] * n
        
        mL = 0
        for i in range(n):
            if height[i] > mL:
                mL = height[i]
            
            maxL[i] = mL

        mR = 0
        for i in reversed(range(n)):
            if height[i] > mR:
                mR = height[i]
            
            maxR[i] = mR
        
        total = 0
        for i in range(n):
            total += min(maxL[i], maxR[i]) - height[i]
        
        return total
        