class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A = nums1 if len(nums1) < len(nums2) else nums2
        B = nums2 if len(nums1) <  len(nums2) else nums1
        total = len(nums1) + len(nums2)


        half = total // 2

        l = 0
        r = len(A) - 1
        while True:
            m = (l + r) // 2
            bm = half - m - 2

            Aleft = A[m] if m >= 0 else float("-infinity")
            Aright = A[m + 1] if (m + 1) < len(A) else float("infinity")
            Bleft = B[bm] if bm >= 0 else float("-infinity")
            Bright = B[bm + 1] if (bm + 1) < len(B) else float("infinity")
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                r = m - 1
            else: 
                l = m + 1
