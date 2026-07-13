class Solution:
    def decodeString(self, s: str) -> str:
        
        stackStrings = []
        stackCounts = []

        k = 0
        cur = ""

        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == "[":
                stackStrings.append(cur)
                stackCounts.append(k)
                cur = ""
                k = 0
            elif char == "]":
                temp = cur
                cur = stackStrings.pop()
                count = stackCounts.pop()
                cur += temp * count
            else:
                cur += char

        return cur