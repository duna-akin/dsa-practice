class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        NROWS = len(matrix)
        NCOLS = len(matrix[0])

        l = 0
        r = NROWS - 1
        while l <= r:
            m = (l + r) // 2

            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                break

        if not (l <= r):
            return False

        row = (l + r) // 2
        l = 0
        r = NCOLS - 1
        while l <= r:
            m = (l + r) // 2
            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True
        return False
            
        