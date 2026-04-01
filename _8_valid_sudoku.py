from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rmap = defaultdict(set)
        cmap = defaultdict(set)
        smap = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[r])):
                val = board[r][c]
                if val == '.':
                    continue
                else:
                    if val in rmap[r] or val in cmap[c] or val in smap[(r // 3, c // 3)]:
                       return False
                    else:
                        rmap[r].add(val)
                        cmap[c].add(val)
                        smap[(r // 3 , c//3)].add(val)
        return True