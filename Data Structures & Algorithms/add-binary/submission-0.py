class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0

        # reversing to make the math work 
        a, b = a[::-1], b[::-1]

        # choose the biggest one to make sure we get every 
        # digit
        for i in range(max(len(a), len(b))):
            
            # if the digit is in bounds get it, otherwise its 0
            # ord(a[i]) - ord("0") converts string "1" or "0" to int 1 or 0
            digitA = ord(a[i]) - ord("0")  if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digitA + digitB + carry

            # want mod 2 as base 2, ensures that 
            # we always get the right value 
            char = str(total % 2)

            res = char + res

            # this operation makes 2 and 3 give carry of 1
            carry = total // 2
        
        if carry:
            res = "1" + res

        return res