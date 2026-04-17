class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (j - i) // 2 + i
            if nums[mid] > target:
                j = mid - 1
            elif nums[mid] < target:
                i = mid + 1
            else:
                return mid
        
        
        return max(mid, i, j)
        
# [-1,0,2,4,6,8]
#             j
#             i
        