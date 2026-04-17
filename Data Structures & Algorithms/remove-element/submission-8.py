class Solution:
    #              
    #nums= [0,1,2,2,3,0,4,2
    #.          ^   ^
    #val=2

    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k


        