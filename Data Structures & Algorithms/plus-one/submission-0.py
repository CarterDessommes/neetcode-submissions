class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            digit = digits[i]
            if digit != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
        return digits
            
            



        