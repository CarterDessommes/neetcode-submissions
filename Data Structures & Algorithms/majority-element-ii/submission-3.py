class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # booyer moore voting alg but just on two numbers
        # as only two numbers can appear more the one third
        # of the total length times. O(1) space
        n = len(nums)
        cnt1 = cnt2 = 0
        num1 = num2 = -1

        # first scan finds two most frequent elements
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = num
                cnt1 = 1
            elif cnt2 == 0:
                num2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        # second scan determines their total counts
        cnt1 = cnt2 = 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
        
        # then we check if each one meets our criteria
        # and add to result if it does
        res = []
        if cnt1 > n // 3:
            res.append(num1)
        if cnt2 > n // 3:
            res.append(num2)
        
        return res

# -- Simpler o(n) space solution simply using a counter --
# target = len(nums) // 3

# counts = Counter(nums)

# sol = []
# for val in counts:
#     if counts[val] > target:
#         sol.append(val)

# return sol

