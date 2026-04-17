class Solution:
    def isPalindrome(self, s: str) -> bool:

        end = len(s) - 1
        start = 0

        while start <= end:
            if not s[end].isalnum():
                end -= 1
            elif not s[start].isalnum():
                start += 1
            elif s[start].lower() != s[end].lower():
                return False
            else:
                end -= 1
                start += 1
            
        
        return True



    # "Was it a car or a cat I saw?"
    #       ^              ^