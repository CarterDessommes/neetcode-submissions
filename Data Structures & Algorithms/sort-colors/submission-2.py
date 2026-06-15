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
                # we can increment i as we know that the value we are swapping with 
                # has already been processed by i so we know  when we access the left
                # pointer it has to be pointing at a 1 as if it where 0 or 2 it 
                # would have already been moved.
            elif num == 2:
                swap(i, r)
                r -= 1
                # we don't increment i here as we will need to make
                # sure that the value we swapped in is not a 0
            else:
                i += 1
                # dont swap the ones so just move forward.

        # the idea for the one pass solution is that we can just partition our 
        # array since we are only sorting three values. we maintaing the insertion
        # point pointers for the 0 and 2 values.


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
