class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # will use // 3 for key (r // 3, c // 3)

        # iterate over the grid
        for r in range(9):
            for c in range(9):

                # skip empty cell
                if board[r][c] == ".":
                    continue

                # check duplicates
                if (board[r][c] in rows[r] or 
                    board[r][c] in columns[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                columns[c].add(board[r][c]) # add current value to c column
                rows[r].add(board[r][c]) # add current value to r column
                squares[(r // 3, c // 3)].add(board[r][c]) # add current value to r//3,c//3 square

        return True
                
