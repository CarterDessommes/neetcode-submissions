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
            
            q.append(r)

            if q[0] < l:
                q.popleft()

            if r + 1 >= k:
                l += 1
                output.append(nums[q[0]])






        return output
            


        