class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_volume = 0
        
        # we can intitialize our pointers on the far ends, that way the 
        # distance aka the width of our container is strictly decreasing
        # that way, we know the only way to get a container that can hold more volumne is by 
        # mopving the smaller of the two pointers inwards.
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
        




            

        