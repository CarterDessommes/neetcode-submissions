class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            len_s = len(s)
            encoding = f"{len_s}#{s}"
            result.append(encoding)
        
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            for j in range(i + 1, len(s)):
                char = s[j]

                if char == "#":
                    length = int(s[i:j])
                    word = s[j+1:j+1+length]
                    res.append(word)
                    i = j+1+length
                    break

            
            
        
        return res
