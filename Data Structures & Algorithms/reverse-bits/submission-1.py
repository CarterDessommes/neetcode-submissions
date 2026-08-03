class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # loop over all possible bit positions
        # 32 bit integer
        for i in range(32):
            # shift desired bit all the way to the right
            # and and it with one to extract it
            bit = (n >> i) & 1
            # then, shift it all the way to the left and 
            # add it to the solution
            res += (bit << (31 - i))
        
        return res

        