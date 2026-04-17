class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start <= end:
            if s[start] != s[end]:
                return self.helper(s[:start] + s[start + 1:]) or self.helper(s[:end] + s[end + 1:])
            start += 1
            end -= 1
        return True

    def helper(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
        