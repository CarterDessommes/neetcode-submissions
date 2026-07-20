class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # sliding window
        # window is valid as long as window size - count <= k

        maxf = 0
        freqs = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(s)):
            # update the freq of the char
            char = s[r]
            freqs[char] += 1

            # update our max frequency if needed
            maxf = max(maxf, freqs[char])
            
            # shrink down invalid windows
            # windows are invalid if 
            # the size is larger than making 
            # changes would allow
            while (r - l + 1) > k + maxf:
                freqs[s[l]] -= 1
                l += 1
            
            # update our result with the current window
            # size
            res = max(res, (r - l + 1))
        
        return res