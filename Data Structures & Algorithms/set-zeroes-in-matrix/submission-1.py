class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # have to have a boolean to represent this as 
        # we can't have the origin represetning two things
        rowZero = False

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                # if its a zero, set its inidcator to zero
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    elif r == 0:
                        rowZero = True

        # go through and set all needed rows and cols to zero
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):

                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # handle if the first column is a zero
        if matrix[0][0] == 0:
            for r in range(len(matrix)):
                matrix[r][0] = 0

        # handle if the first row was a zero
        if rowZero:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        




        

    
    
        
        