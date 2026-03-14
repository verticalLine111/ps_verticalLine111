from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        squareMap = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                val = board[r][c]
                if val == '.':
                    continue

                if (val in rowMap[r]
                    or val in colMap[c]
                    or val in squareMap[(r // 3, c // 3)]):
                    return False

                rowMap[r].add(val)
                colMap[c].add(val)
                squareMap[(r // 3, c // 3)].add(val)
        return True