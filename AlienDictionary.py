"""
There is a new alien language which uses the latin alphabet.
However, the order among letters are unknown to you.
You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"

Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"

Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".

Note:

    You may assume all letters are in lowercase.
    You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
    If the order is invalid, return an empty string.
    There may be multiple valid order of letters, return any one of them is fine.


"""
class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # topology sort
        g = collections.defaultdict(set)
        indegree = dict()
        for word in words:
            for c in word:
                if c not in indegree:
                    indegree[c] = 0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                index = 0
                while index<min(len(words[i]),len(words[j])):
                    if words[i][index]!=words[j][index]:
                        # check if there is cycle
                        if words[i][index] in g[words[j][index]]:
                            return ""
                        if words[j][index] not in g[words[i][index]]:
                            indegree[words[j][index]] += 1
                            g[words[i][index]].add(words[j][index])
                        break
                    index += 1

        #print(g)
        #print(indegree)
        ret = ""
        q = collections.deque()
        for k in indegree:
            if indegree[k]==0:
                q.append(k)
        while len(q):
            cur = q.popleft()
            ret += cur
            for neighbor in g[cur]:
                indegree[neighbor] -= 1
                if indegree[neighbor]==0:
                    q.append(neighbor)
            g.pop(cur)
        return ret
