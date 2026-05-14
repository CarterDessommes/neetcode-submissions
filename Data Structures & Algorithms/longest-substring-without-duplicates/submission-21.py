class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0

        best = 0
        for r in range(len(s)):
            # if we hav ethis val in seen
            # move left  over untill its not in seen
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            else:
                seen.add(s[r])
                
                
            r += 1
            best = max(best, r - l)
        
        return best


        

        






