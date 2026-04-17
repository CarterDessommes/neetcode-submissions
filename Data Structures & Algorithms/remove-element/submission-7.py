class Solution:
    #              V
    #nums=[0,1,4,0,3,2,2,2]
    #.               ^
    #val=2

    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k



        