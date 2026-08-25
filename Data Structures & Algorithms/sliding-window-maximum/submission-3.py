class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        # q has decreasing values but increasing indexes
        q = deque()
        l = 0

        for r in range(len(nums)):
            # pop of everything smaller than this val
            # so q has bigger values at the front
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # add current index
            q.append(r)

            # remove largest value (and lowest index)
            # if it is now out of hte window
            if q[0] < l:
                q.popleft()

            # if our window is the right size, add output
            # and move it over
            if r + 1 >= k:
                l += 1
                output.append(nums[q[0]])

        return output
            


        