import collections
"""
Given two words (beginWord and endWord), and a dictionary's word list,
find all shortest transformation sequence(s) from beginWord to endWord, such that:

1. Only one letter can be changed at a time
2. Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
1. Return an empty list if there is no such transformation sequence.
2. All words have the same length.
3. All words contain only lowercase alphabetic characters.
4. You may assume no duplicates in the word list.
5. You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def dfs(g, dist, path, endWord, ret):
            cur = path[-1]
            if cur==endWord:
                ret.append(path)
                return
            for nxt in g[cur]:
                #print(path,nxt)
                if dist[nxt]==dist[cur]+1:
                    dfs(g,dist,path+[nxt],endWord,ret)

        g = collections.defaultdict(set)
        dist = dict()
        wordSet = set(wordList)
        q = collections.deque([[beginWord,0]])
        dist[beginWord] = 0
        while len(q)>0:
            cur,step = q.popleft()
            if endWord in dist and dist[endWord]<step:
                break
            for i in range(len(cur)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c!=cur[i]:
                        nxt = cur[:i]+c+cur[i+1:]
                        if nxt in wordSet:
                            g[cur].add(nxt)
                            if nxt not in dist:
                                dist[nxt] = step+1
                                q.append([nxt,step+1])
        #print(g, dist)
        if endWord not in dist:
            return []
        ret = []
        dfs(g, dist, [beginWord], endWord, ret)
        return ret
