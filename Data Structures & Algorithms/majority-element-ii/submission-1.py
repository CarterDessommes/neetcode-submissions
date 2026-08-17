class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # target = len(nums) // 3

        # counts = Counter(nums)

        # sol = []
        # for val in counts:
        #     if counts[val] > target:
        #         sol.append(val)
        
        # return sol
        
        # o(1) space uses boyer moore voting

        n = len(nums)
        num1 = num2 = -1
        cnt1 = cnt2 = 0

        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                cnt1 = 1
                num1 = num
            elif cnt2 == 0:
                cnt2 = 1
                num2 = num
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1 = cnt2 = 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
        
        res = []
        if cnt1 > n // 3:
            res.append(num1)
        if cnt2 > n // 3:
            res.append(num2)
        
        return res