class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        count = 0

        # the idea here is just loop through the 
        # whole string and try each location
        # as the centerpoint of a possible palindrome.
        # the catch is palidromes can be both even and odd in length
        # so we need to consider both of these possibilites when 
        # evaluating each point as a center.
        # time complexity is O(n^2) and space is O(1)
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
