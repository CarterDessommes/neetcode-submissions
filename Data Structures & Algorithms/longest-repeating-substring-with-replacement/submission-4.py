class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # sliding window
        # window is valid as long as window size - count <= k

        maxf = 0
        freqs = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(s)):
            char = s[r]
            freqs[char] += 1
            print(f"saw {char}, freq now {freqs[char]}")

            if freqs[char] > maxf:
                print(f"updating max {char}: {freqs[char]}")
                maxf = freqs[char]
            
            while (r - l + 1) - maxf > k:
                print("shrinking")
                freqs[s[l]] -= 1
                l += 1
            
            print(f"res: {res}, window size: {r - l + 1}")
            res = max(res, (r - l + 1))
        
        return res