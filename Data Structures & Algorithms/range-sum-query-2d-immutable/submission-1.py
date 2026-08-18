class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sum_matrix = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        # maintain a a 2d prefix sum where each grid in the matrix
        # basically says this is the value of the rectangle with r, c as bottom right corner
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                left = self.sum_matrix[r + 1][c]
                up = self.sum_matrix[r][c + 1]
                overlap = self.sum_matrix[r][c]
                self.sum_matrix[r + 1][c + 1] = matrix[r][c] + left + up - overlap
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # find the value by subtracting anything above and to the left
        # noting that there will be a bit of overlap you subtract off twice so you must add id back
        overlap = self.sum_matrix[row1][col1]
        bottom_right = self.sum_matrix[row2 + 1][col2 + 1]

        above = self.sum_matrix[row1][col2 + 1]
        left = self.sum_matrix[row2 + 1][col1]

        final = bottom_right - above - left + overlap
        return final

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)