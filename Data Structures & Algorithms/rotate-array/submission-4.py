class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        k %= n + 1

        self.reverse(nums, 0, n) 
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n)



    def reverse(self, arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            r -= 1
            l += 1





        # o(n) extra space version
        # res = [0] * len(nums)
        # for i in range(len(nums)):
        #     new_i = (i + k) % len(nums)
        #     res[new_i] = nums[i]
        
        # for i in range(len(nums)):
        #     nums[i] = res[i]




        


        
