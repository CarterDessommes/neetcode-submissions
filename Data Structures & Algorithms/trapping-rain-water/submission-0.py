class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        maxLeft = [0] * n
        maxRight = [0] * n

        maxL = 0
        for i in range(len(height)):
            cur = height[i]
            if cur > maxL:
                maxL = cur
            maxLeft[i] = maxL
        
        maxR = 0
        for i in reversed(range(len(height))):
            cur = height[i]
            if cur > maxR:
                maxR = cur
            maxRight[i] = maxR
        
        res = 0
        for i in range(n):
            res += min(maxLeft[i], maxRight[i]) - height[i]
        return res


        