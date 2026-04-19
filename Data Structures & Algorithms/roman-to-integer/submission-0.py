class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0

        conversion = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        for i in range(len(s)):
            char = s[i]
            nxt = None
            if i < len(s) - 1:
                nxt = s[i + 1]

            if char == "I":
                if nxt == "V" or nxt == "X":
                    ans += -conversion[char]
                else: 
                    ans += conversion[char]

            elif char == "X":
                if nxt == "L" or nxt == "C":
                    ans += -conversion[char]
                else: ans += conversion[char]

            elif char == "C":
                if nxt == "D" or nxt == "M":
                    ans += -conversion[char]
                else: ans += conversion[char]
            else:
                ans += conversion[char]

        return ans
        