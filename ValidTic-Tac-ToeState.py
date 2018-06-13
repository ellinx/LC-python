"""
A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

    Players take turns placing characters into empty squares (" ").
    The first player always places "X" characters, while the second player always places "O" characters.
    "X" and "O" characters are always placed into empty squares, never filled ones.
    The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
    The game also ends if all squares are non-empty.
    No more moves can be played if the game is over.

Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true

Note:

    board is a length-3 array of strings, where each string board[i] has length 3.
    Each board[i][j] is a character in the set {" ", "X", "O"}.

"""
class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        xNum, oNum = 0, 0
        for i in range(3):
            for j in range(3):
                if board[i][j]=='X':
                    xNum += 1
                if board[i][j]=='O':
                    oNum += 1
        if oNum>xNum:
            return False
        if xNum-oNum>1:
            return False
        # win case: 0-2 row, 3-5 col 6-7 diag
        xWin, oWin = [], []
        # check rows
        for i in range(3):
            if board[i].count('X')==3:
                xWin.append(i)
            if board[i].count('O')==3:
                oWin.append(i)
        # check cols
        for i in range(3):
            xCount, oCount = 0, 0
            for j in range(3):
                if board[j][i]=='X':
                    xCount += 1
                if board[j][i]=='O':
                    oCount += 1
            if xCount==3:
                xWin.append(3+i)
            if oCount==3:
                oWin.append(3+i)
        # check diags
        xCount, oCount = 0, 0
        for i in range(3):
            if board[i][i]=='X':
                xCount += 1
            if board[i][i]=='O':
                oCount += 1
        if xCount==3:
            xWin.append(6)
        if oCount==3:
            oWin.append(6)
        xCount, oCount = 0, 0
        for i in range(3):
            if board[i][2-i]=='X':
                xCount += 1
            if board[i][2-i]=='O':
                oCount += 1
        if xCount==3:
            xWin.append(7)
        if oCount==3:
            oWin.append(7)
        if len(xWin) and len(oWin):
            return False
        if len(xWin):
            if xNum==oNum:
                return False
            if len(xWin)==2:
                if (xWin[0] in (0,1,2) and xWin[1] in (0,1,2)) or (xWin[0] in (3,4,5) and xWin[1] in (3,4,5)):
                    return False
        if len(oWin):
            if xNum-oNum==1:
                return False
            if len(oWin)==2:
                if (oWin[0] in (0,1,2) and oWin[1] in (0,1,2)) or (oWin[0] in (3,4,5) and oWin[1] in (3,4,5)):
                    return False
        return True
