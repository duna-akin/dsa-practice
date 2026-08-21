class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # len(matrix) -> count of rows
        # len(matrix[n]) -> count of columns

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == target: return True
        return False