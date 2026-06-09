class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_volume = 0

        # height=[1,7,2,5,4,7,3,6]  
        #           ^           ^
        # hl = 7
        # hr = 6
        # dist = 5
        # mv = 30
        
        while left < right and right < len(heights) and left >= 0:
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
        




            

        