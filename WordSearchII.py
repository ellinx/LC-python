"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

Example:

Input:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = dict()

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def insertWord(root, word):
            for c in word:
                if c not in root.children:
                    root.children[c] = TrieNode()
                root = root.children[c]
            root.isWord = True

        def dfs(root, board, i, j, cur, used, ret):
            if board[i][j] not in root.children:
                return
            nxtNode = root.children[board[i][j]]
            cur += board[i][j]
            if nxtNode.isWord:
                ret.append(cur)
                nxtNode.isWord = False
            used.add((i,j))
            dirs = [[-1,0],[1,0],[0,-1],[0,1]]
            m, n = len(board), len(board[0])
            for each in dirs:
                ni = i+each[0]
                nj = j+each[1]
                if ni>=0 and ni<m and nj>=0 and nj<n and (ni,nj) not in used:
                    dfs(nxtNode, board, ni, nj, cur, used, ret)
            used.remove((i,j))

        root = TrieNode()
        for word in words:
            insertWord(root, word)
        m, n = len(board), len(board[0])
        ret = []
        for i in range(m):
            for j in range(n):
                dfs(root, board, i, j, "", set(), ret)
        return ret
