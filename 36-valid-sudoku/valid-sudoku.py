class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Initialize dictionaries for columns, rows, and squares to keep track of seen numbers.
        # Use defaultdict to automatically create an empty set for new keys.
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        # Iterate over each cell in the 9x9 board.
        for r in range(9):
            for c in range(9):
                # Read the value of the current cell.
                cell = board[r][c]
                # Skip if the cell is empty (denoted by '.').
                if cell == ".":
                    continue
                
                # Calculate the index for the 3x3 square to which the cell belongs.
                # Integer division by 3 groups the indices for rows and columns into 3 parts each.
                square_index = (r // 3, c // 3)
                
                # Check if the cell value is already present in the current row, column, or square.
                # If so, the Sudoku board is invalid.
                if cell in rows[r] or cell in cols[c] or cell in squares[square_index]:
                    return False  # The board is invalid
                
                # Add the cell value to the sets corresponding to the current row, column,
                # and square to keep track of seen numbers.
                cols[c].add(cell)
                rows[r].add(cell)
                squares[square_index].add(cell)
        
        # If no duplicates are found after checking all cells, the board is valid.
        return True

                