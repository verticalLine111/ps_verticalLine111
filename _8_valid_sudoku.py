from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # return False # 중간에 뭔가 이슈가 있다면
        for line in board:
            countMap = {}
            for blankIdx in range(len(line)):
                if self.isNumeric(line[blankIdx]) and line[blankIdx] in countMap:
                    # 숫자가 2번 나온 경우가 됨
                    return False
                else:
                    if self.isNumeric(line[blankIdx]):
                        countMap[line[blankIdx]] = 1
        # 세로로 한번
        # 3x3에서 한번
        verticalIdx = 0
        while verticalIdx < len(board[0]):
            countMap = {}
            idx = 0  # 위에서부터
            for idx in range(0, 8, 1):
                if self.isNumeric(board[idx][verticalIdx]) and board[idx][verticalIdx] in countMap:
                    return False
                else:
                    if self.isNumeric(board[idx][verticalIdx]):
                        countMap[board[idx][verticalIdx]] = 1
            verticalIdx += 1

        partialIdx = 0
        totalCount = 0
        while totalCount < len(board):
            lineSet = set()
            list(set(*board[partialIdx][0:3]))

            board[partialIdx][0:3]
            board[partialIdx][0:3]

            totalCount += 1
        # 자 이제 3/3
        # print(board[0][0:3])
        # print(board[1][0:3])
        # print(board[2][0:3])
        # 얘네가 한 세트

        return True  # valid 하다면

    def isNumeric(self, c: str) -> bool:
        return '0' <= c and c <= '9'
# 튜플로 빼서 길이가 다르면 ? 중복이 제거가 되어서 그런거라고 볼 수 있지 않나
# 아 set으로
# ["1","2",".",".","3",".",".",".","."]
# ["4",".",".","5",".",".",".",".","."]
# [".","9","1",".",".",".",".",".","3"]
# ["5",".",".",".","6",".",".",".","4"]
# [".",".",".","8",".","3",".",".","5"]
# ["7",".",".",".","2",".",".",".","6"]
# [".",".",".",".",".",".","2",".","."]
# [".",".",".","4","1","9",".",".","8"]
# [".",".",".",".","8",".",".","7","9"]

