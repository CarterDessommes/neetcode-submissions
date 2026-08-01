class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        #steps[0] is how many moves left in the horizontal direction
        #steps[1] is how many moves left in the vertical direction
        steps = [len(matrix[0]), len(matrix) - 1]
        

        # d is direction, 0, 1, 2, or 3
        # 0 is right, 1 is down, 2 is left, 3 is up
        r, c, d = 0, -1, 0

        # this is a cool trick to 
        # alter which index of steps we are looking at
        # so if the direction is right, or 0, we look at 0th index.
        # and so on
        while steps[d & 1]:
            # 
            for i in range(steps[d & 1]):
                r += directions[d][0]
                c += directions[d][1]
                res.append(matrix[r][c])
            steps[d & 1] -= 1
            d += 1 
            d %= 4
        return res


        

        