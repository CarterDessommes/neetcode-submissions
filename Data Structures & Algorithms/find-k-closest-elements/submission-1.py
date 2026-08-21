class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:


        l, r = 0, len(arr) - k
        while l < r:
            m = (l + r) // 2
            # if element at the prospective start is 
            # furhter from the target value than the element right after
            # the array, then we must shfift the array right
            if abs(arr[m] - x) > abs(arr[m + k] - x):
                l = m + 1
            # otherwise the element at the start is closer, 
            # so the start of the array must be at or before
            # this index
            else:
                r = m
        
        return arr[l:l + k]