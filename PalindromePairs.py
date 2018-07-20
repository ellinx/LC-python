"""
 Given a list of unique words, find all pairs of distinct indices (i, j) in the given list,
 so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]

Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""
class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ret = []
        wordToIndex = dict()
        for i in range(len(words)):
            wordToIndex[words[i]] = i
        for i in range(len(words)):
            for j in range(len(words[i])+1):
                s1 = words[i][:j]
                s2 = words[i][j:]
                rs1 = s1[::-1]
                rs2 = s2[::-1]
                #print(i,s1,s2)
                if s1==rs1:
                    if rs2 in wordToIndex and wordToIndex[rs2]!=i:
                        ret.append([wordToIndex[rs2], i])
                if len(s2) and s2==rs2:
                    if rs1 in wordToIndex and wordToIndex[rs1]!=i:
                        ret.append([i, wordToIndex[rs1]])
        return ret
