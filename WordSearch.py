"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


"""
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(board, word, start, i, j, visited):
            if word[start]!=board[i][j]:
                return False
            if len(word)==start+1:
                return True
            visited[i][j] = True
            dirs = [(-1,0),(1,0),(0,-1),(0,1)]
            for each in dirs:
                ni = i + each[0]
                nj = j + each[1]
                if ni>=0 and ni<len(board) and nj>=0 and nj<len(board[0]) and (not visited[ni][nj]):
                    if dfs(board, word, start+1, ni, nj, visited):
                        return True
            visited[i][j] = False
            return False

        m = len(board)
        if m==0:
            return False
        n = len(board[0])
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if dfs(board, word, 0, i, j, visited):
                    return True
        return False
