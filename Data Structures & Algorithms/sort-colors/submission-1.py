class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1

        i = 0

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= r:
            num = nums[i]
            if num == 0:
                swap(l, i)
                l += 1
                i += 1
            elif num == 2:
                swap(i, r)
                r -= 1
            else:
                i += 1




        # -- counting sort solution, but this uses two passes --
        # counts = [0] * 3

        # for num in nums:
        #     counts[num] += 1
        
        # index = 0
        # for i in range(3):
        #     while counts[i]:
        #         counts[i] -= 1
        #         nums[index] = i
        #         index += 1
