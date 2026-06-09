class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_volume = 0
        
        while left < right:
            height_left = heights[left]
            height_right = heights[right]

            dist = right - left

            vol = min(height_left, height_right) * dist

            max_volume = max(max_volume, vol)

            if height_left < height_right:
                left += 1
            else:
                right -= 1
        
        return max_volume
        




            

        