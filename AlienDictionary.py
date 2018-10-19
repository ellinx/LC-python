"""
There is a new alien language which uses the latin alphabet.
However, the order among letters are unknown to you.
You receive a list of non-empty words from the dictionary,
where words are sorted lexicographically by the rules of this new language.
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

1. You may assume all letters are in lowercase.
2. You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
3. If the order is invalid, return an empty string.
4. There may be multiple valid order of letters, return any one of them is fine.


"""
class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        g = collections.defaultdict(set)
        indegree = dict()
        for c in words[0]:
            indegree[c] = 0
        for i in range(1,len(words)):
            idx = 0
            minLen = min(len(words[i-1]), len(words[i]))
            while idx<minLen:
                indegree[words[i][idx]] = indegree.get(words[i][idx], 0)
                if words[i-1][idx]==words[i][idx]:
                    idx += 1
                    continue
                break
            if idx<minLen:
                if words[i][idx] not in g[words[i-1][idx]]:
                    indegree[words[i][idx]] += 1
                    g[words[i-1][idx]].add(words[i][idx])
            while idx<len(words[i]):
                indegree[words[i][idx]] = indegree.get(words[i][idx], 0)
                idx += 1
        #print(indegree)
        ret = ""
        q = collections.deque()
        for k in indegree:
            if indegree[k]==0:
                q.append(k)
        while len(q):
            cur = q.popleft()
            ret += cur
            for adj in g[cur]:
                indegree[adj] -= 1
                if indegree[adj]==0:
                    q.append(adj)
        if len(ret)<len(indegree):
            return ""
        return ret
