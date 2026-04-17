class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cur = nums[0]
        for num in nums:
            if num == cur:
                count += 1
            else:
                count -= 1
                if count == 0:
                    cur = num
                    count = 1
        
        return cur

# [1,2,3,2,2,2,5,4,2]
#      ^
# cur = 2 count = 1
        