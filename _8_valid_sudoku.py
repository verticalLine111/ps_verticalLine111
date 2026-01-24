from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for line in board:
            lineSet = set()
            for idx in range(len(line)):
                if line[idx] == '.':
                    continue
                else:
                    if line[idx] in lineSet:
                        return False
                    else:
                        lineSet.add(line[idx])
        horizonidx = 0
        while horizonidx < len(board):
            vertSet = set()
            for idx in range(len(board)):
                if board[idx][horizonidx] == '.':
                    continue
                else:
                    if board[idx][horizonidx] in vertSet:
                        return False
                    else:
                        vertSet.add(board[idx][horizonidx])
            horizonidx += 1

        tupleMap = defaultdict(set)
        for i in range(0,3):
            for j in range(0,3):
                tupleMap[(i,j)] = set()
        for i in range(len(board)):
            for j in range(len(board)):
                key = (int(i / 3) , int(j/3))
                if board[i][j] == '.':
                    continue
                if board[i][j] in tupleMap[key]:
                    return False
                else:
                    tupleMap[key].add(board[i][j])
        return True
