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
    def __init__(self):
        self.root = TrieNode()

    def insertWord(self, words):
        cur = self.root
        for c in words:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def dfs(board, visited, curStr, curNode, i, j, ret):
            if board[i][j] not in curNode.children:
                return
            curNode = curNode.children[board[i][j]]
            curStr += board[i][j]
            if curNode.isWord:
                ret.add(curStr)
            visited[i][j] = True
            #up
            if i and not visited[i-1][j]:
                dfs(board, visited, curStr, curNode, i-1, j, ret)
            #down
            if i<len(board)-1 and not visited[i+1][j]:
                dfs(board, visited, curStr, curNode, i+1, j, ret)
            #left
            if j and not visited[i][j-1]:
                dfs(board, visited, curStr, curNode, i, j-1, ret)
            #right
            if j<len(board[0])-1 and not visited[i][j+1]:
                dfs(board, visited, curStr, curNode, i, j+1, ret)
            visited[i][j] = False

        for word in words:
            self.insertWord(word)
        ret = set()
        visited = [[False]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, visited, "", self.root, i, j, ret)
        return list(ret)
