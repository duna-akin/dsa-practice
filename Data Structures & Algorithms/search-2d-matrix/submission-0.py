class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top, bot = 0, m - 1

        while top <= bot:
            midRow = (top + bot) // 2
            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bot = midRow - 1
            else:
                break
        if top > bot: return False

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[midRow][mid] < target:
                l = mid + 1
            elif matrix[midRow][mid] > target:
                r = mid - 1
            else:
                return True
        return False