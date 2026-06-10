class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # bounds of the problem allow k > n, in which case just wrap
        # it around
        k %= n

        # built on the observation that reversing the whole array,
        # then the first k elements, and then the last n - k elements
        # will produce the desired rotated array.
        self.reverse(nums, 0, n - 1) 
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)



    def reverse(self, arr, l, r):
        # simple reverse function that just swaps positions of elements
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




        


        
