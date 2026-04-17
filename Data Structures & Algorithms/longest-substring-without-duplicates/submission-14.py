class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        # dvdf
        best = 0
        cur = 0
        i = 0
        while i < len(s):
            char = s[i]
            print(f"processing {char}")
            if char in seen:
                best = max(best, cur)
                print(f"seen it, best is now: {best}")
                seen.clear()
                i = i - cur + 1
                cur = 0
            else:
                i += 1
                cur += 1
                print(f"havent seen it, cur is {cur}")
                seen.add(char)
        
        return max(best, cur)




