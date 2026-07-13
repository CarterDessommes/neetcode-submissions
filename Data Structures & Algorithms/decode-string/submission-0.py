class Solution:
    def decodeString(self, s: str) -> str:
        stringStack = []
        countStack = []

        cur = ""
        k = 0

        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == "[":
                stringStack.append(cur)
                countStack.append(k)
                k = 0
                cur = ""
            elif char == "]":
                temp = cur
                cur = stringStack.pop()
                count = countStack.pop()
                cur += temp * count
            else: 
                cur += char
        return cur

            