class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # reverse + rotation = 90 degree rotations
        # good trick to remember!

        matrix.reverse()

        # loop over everything above the diagonal
        for r in range(len(matrix)):
            for c in range(r + 1, len(matrix)):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        


