class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i, j = m - 1, n - 1
        end = n + m - 1

        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[end] = nums1[i]
                i -= 1
            else:
                nums1[end] = nums2[j]
                j -= 1
            end -= 1


       

        
   


# nums1 = [10,20,20,40,0,0]  nums2 = [1,2]
#               
# [10,20,10,20,20,40] [1,2]
#   i  e         j


        