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
    def alienOrder(self, words: 'List[str]') -> 'str':
        if len(words)==1:
            return words[0]
        indegree = dict()
        g = collections.defaultdict(set)
        for i in range(1,len(words)):
            idx = 0
            while idx<len(words[i-1]) and idx<len(words[i]):
                if words[i-1][idx] not in indegree:
                    indegree[words[i-1][idx]] = 0
                if words[i][idx] not in indegree:
                    indegree[words[i][idx]] = 0
                if words[i-1][idx]==words[i][idx]:
                    idx += 1
                    continue
                if words[i][idx] not in g[words[i-1][idx]]:
                    g[words[i-1][idx]].add(words[i][idx])
                    indegree[words[i][idx]] += 1
                break
            for j in range(idx, len(words[i-1])):
                if words[i-1][j] not in indegree:
                    indegree[words[i-1][j]] = 0
            for j in range(idx, len(words[i])):
                if words[i][j] not in indegree:
                    indegree[words[i][j]] = 0
        #print(indegree)
        q = collections.deque()
        for k in indegree:
            if indegree[k]==0:
                q.append(k)
        order = []
        while len(q)>0:
            cur = q.popleft()
            order.append(cur)
            for nxt in g[cur]:
                indegree[nxt] -= 1
                if indegree[nxt]==0:
                    q.append(nxt)
        if len(order)<len(indegree):
            return ""
        return "".join(order)
