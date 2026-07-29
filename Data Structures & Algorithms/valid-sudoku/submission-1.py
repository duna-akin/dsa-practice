class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        # iterate through the cells row by row
        for r in range(9):
            for c in range(9):
                currentVal = board[r][c]

                # skip empty cell
                if currentVal == '.':
                    continue

                # check whether the cell value already exists in any of the respective sets
                if currentVal in rows[r] or currentVal in columns[c] or currentVal in squares[(r // 3, c // 3)]:
                    return False

                # add the value to the respective sets
                rows[r].add(currentVal)
                columns[c].add(currentVal)
                squares[(r // 3, c // 3)].add(currentVal)

        return True