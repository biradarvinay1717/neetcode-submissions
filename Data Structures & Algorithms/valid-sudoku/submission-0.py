import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use dictionaries of sets to track numbers seen in each area
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) # Key: (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # 1. Determine the square coordinate (0-2, 0-2)
                square_coord = (r // 3, c // 3)
                
                # 2. Check if the value already exists in this row, col, or square
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[square_coord]):
                    return False
                
                # 3. Add the value to the sets
                rows[r].add(val)
                cols[c].add(val)
                squares[square_coord].add(val)
                
        return True