class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.sum_matrix = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        # build a 2d prefix sum array, where r c is the sum of the rectangle with bottom right corner r c
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                left = self.sum_matrix[r + 1][c]
                up = self.sum_matrix[r][c + 1]
                overlap = self.sum_matrix[r][c]

                # node adding left and up will double count the overlapping area so subtract it off
                self.sum_matrix[r + 1][c + 1] = matrix[r][c] + left + up - overlap
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.sum_matrix[row2 + 1][col1]
        up = self.sum_matrix[row1][col2 + 1]
        overlap = self.sum_matrix[row1][col1]
        # now to find our answers, just find r, c then subtract the rectangle above and to the left of it
        # noting that this will subtracy an overlapping area two times so you must add it back
        return self.sum_matrix[row2 + 1][col2 + 1] - left - up + overlap

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)