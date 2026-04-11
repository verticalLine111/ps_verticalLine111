class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        sqa = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[r])):
                val = board[r][c]
                if val == '.':
                    continue
                if val in row[r] or val in col[c] or val in sqa[(r // 3, c // 3)]:
                    return False
                else:
                    row[r].add(val)
                    col[c].add(val)
                    sqa[(r // 3 , c // 3)].add(val)
        return True