"""
Given two sentences words1, words2 (each represented as an array of strings),
and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar,
if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive.
For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric.
For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself.
For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words.
So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:
The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].
"""
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        def findRoot(roots, w):
            if w not in roots:
                roots[w] = w
                return w
            while roots[w]!=w:
                w = roots[w]
            return w

        if len(words1)!=len(words2):
            return False
        roots = dict()
        for w1, w2 in pairs:
            root1 = findRoot(roots, w1)
            roots[w1] = root1
            root2 = findRoot(roots, w2)
            roots[w2] = root2
            roots[root1] = root2
        for i in range(len(words1)):
            root1 = findRoot(roots, words1[i])
            root2 = findRoot(roots, words2[i])
            if root1!=root2:
                return False
        return True


class Solution2:
    #BFS
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        def bfs(g, s1, s2):
            q = collections.deque()
            visited = set()
            q.append(s1)
            visited.add(s1)
            while len(q):
                cur = q.popleft()
                if cur==s2:
                    return True
                for each in g[cur]:
                    if each not in visited:
                        visited.add(each)
                        q.append(each)
            return False

        if len(words1)!=len(words2):
            return False
        g = collections.defaultdict(set)
        for pair in pairs:
            g[pair[0]].add(pair[1])
            g[pair[1]].add(pair[0])
        for i in range(len(words1)):
            if words1[i]!=words2[i] and not bfs(g, words1[i], words2[i]):
                return False
        return True
