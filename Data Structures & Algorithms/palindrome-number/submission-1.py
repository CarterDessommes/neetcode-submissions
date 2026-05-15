class Solution:
    def isPalindrome(self, x: int) -> bool:
        # neg numbers of numbers that end in 0 can't be 
        # palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0
        while rev < x:
            # add the last digit of x onto rev
            rev = (rev * 10) + (x % 10)
            # remove the last digit of x
            x = x // 10 
        return rev == x or x == rev // 10

        