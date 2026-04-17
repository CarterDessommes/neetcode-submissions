class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        best = 0


        # the idea is that we have left and right pointers. we are moving 
        # right to the right untill we see a dupe, then we move left over untill
        # we remove the dupe, saving the best length we  at each iteration.
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            best = max(best, r - l + 1)
        
        return best






