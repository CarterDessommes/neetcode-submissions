class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        count = 0
        for i in range(len(s)):
            

            # even length
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            # odd length
            l = i
            r = i
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
        return count
