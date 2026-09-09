class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            mid = nums[m]
            right = nums[r]
            left = nums[l]

            if mid == target:
                return True
            
            # if left is sorted
            if left < mid:
                # if its in the left
                if left <= target < mid:
                    r = m - 1
                else:
                    l = m + 1

            # if right is sorted
            elif left > mid:
                # if its in the right
                if mid < target <= right:
                    l = m + 1
                else:
                    r = m - 1
            
            # else left == mid and we know its not the target
            # so we can safely just skip this one
            else: 
                l += 1
        
        return False
            


