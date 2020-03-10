# 在一个 8 x 8 的棋盘上，有一个白色车（rook）。也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。它们分别以字符 “R”，“.”，“B
# ” 和 “p” 给出。大写字符表示白棋，小写字符表示黑棋。 
# 
#  车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜
# 色相反的卒。另外，车不能与其他友方（白色）象进入同一个方格。 
# 
#  返回车能够在一次移动中捕获到的卒的数量。 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",
# ".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",
# ".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".",
# "."],[".",".",".",".",".",".",".","."]]
# 输出：3
# 解释：
# 在本例中，车能够捕获所有的卒。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：[[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".",
# "p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B",
# "p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".",
# "."],[".",".",".",".",".",".",".","."]]
# 输出：0
# 解释：
# 象阻止了车捕获任何卒。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",
# # ".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",
# # ".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".",
# # "."],[".",".",".",".",".",".",".","."]]
# 输出：3
# 解释： 
# 车可以捕获位置 b5，d6 和 f5 的卒。
#  
# 
#  
# 
#  提示： 
# 
#  
#  board.length == board[i].length == 8 
#  board[i][j] 可以是 'R'，'.'，'B' 或 'p' 
#  只有一个格子上存在 board[i][j] == 'R' 
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        '''
        首先找到车所在的行和列
        然后根据所在的行和列匹配车所能捕获的卒数
        '''
        output = 0
        col = None
        row = None
        for i in range(len(board)):
            if 'R' in board[i]:
                row = i
                break
        col = board[row].index('R')
        s = ''.join(board[row])
        s = s.replace('.', '')
        if 'pR' in s:
            output += 1
        if 'Rp' in s:
            output += 1
        s = ''.join([i[col] for i in board])
        s = s.replace('.', '')
        if 'pR' in s:
            output += 1
        if 'Rp' in s:
            output += 1
        return output


    def numRookCaptures1(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        Origin = [0, 0]
        for i, row in enumerate(board):
            for j, line in enumerate(row):
                if line == "R":
                    Origin[0] = i
                    Origin[1] = j
        # print(Origin) # 找到 R 的坐标 Origin[i, j]
        counter = 0

        # 有 Origin 出发，分别朝向东南西北四个方向扫描：
        # East
        row = Origin[0]
        line = Origin[1]
        for i in range(line + 1, 8):
            if board[row][i] == "p":
                counter += 1
                break
            elif board[row][i] == ".":
                continue
            else:
                break
        # West
        row = Origin[0]
        line = Origin[1]
        for i in range(line - 1, 0, -1):
            if board[row][i] == "p":
                counter += 1
                break
            elif board[row][i] == ".":
                continue
            else:
                break
        # South
        row = Origin[0]
        line = Origin[1]
        for i in range(row - 1, 0, -1):
            if board[i][line] == "p":
                counter += 1
                break
            elif board[i][row] == ".":
                continue
            else:
                break
        # North
        row = Origin[0]
        line = Origin[1]
        for i in range(row + 1, 8):
            if board[i][line] == "p":
                counter += 1
                break
            elif board[i][row] == ".":
                continue
            else:
                break
        return counter


# leetcode submit region end(Prohibit modification and deletion)
board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".",
                                                                                              ".", ".", "p", ".", ".",
                                                                                              ".", "."],
         ["p", "p", ".", "R", ".", "p", "B", "."], [".", ".", ".", ".",
                                                    ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".",
          "."], [".", ".", ".", ".", ".", ".", ".", "."]]

print(Solution().numRookCaptures(board))
