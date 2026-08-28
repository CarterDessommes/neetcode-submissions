class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        # maintain a stack where the bars are in increasing order
        stack = []

        # for each bar we wanna know how wide it can stretch while still being
        # the shortest bar in that rectange
        for i in range(n + 1):
            # when we see a shorter bar, it means the 
            # bar on the top of the stack cant extend further right
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                # pop it as the height of a rectange
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            # if the next bar is taller or equal, push index
            stack.append(i)
        
        return maxArea        