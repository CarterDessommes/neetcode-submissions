class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return ""
        
        n = columnNumber - 1
        prefix = self.convertToTitle(n // 26)
        suffix = chr(ord('A') + n % 26)

        return prefix + suffix

        

        