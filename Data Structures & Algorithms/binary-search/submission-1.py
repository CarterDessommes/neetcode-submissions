class Solution:
    def search(self, nums: List[int], target: int) -> int:
        j = len(nums) - 1
        i = 0
        while i <= j:
            mid = (j - i) // 2 + i
            if nums[mid] > target:
                j = mid - 1
            elif nums[mid] < target:
                i = mid + 1
            else: 
                return mid

        return -1


        # [-1,0,2,4,6,8] mid == 2, target = 3
        #       i j    
        #.      m
       
        