class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # build a res of opposite dimension, so instead of rxc is cxr.
        res = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        # do the needed swaps
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res[c][r] = matrix[r][c]
        
        return res


        