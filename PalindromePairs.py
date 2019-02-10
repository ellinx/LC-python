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
    def palindromePairs(self, words: 'List[str]') -> 'List[List[int]]':
        def isPalindrome(s):
            l, r = 0, len(s)-1
            while l<r:
                if s[l]!=s[r]:
                    return False
                l += 1
                r -= 1
            return True

        wordIdx = dict()
        n = len(words)
        for i in range(n):
            wordIdx[words[i]] = i
        ret = []
        for i in range(n):
            if isPalindrome(words[i]) and "" in wordIdx and wordIdx[""]!=i:
                ret.append([wordIdx[""], i])
            for j in range(len(words[i])):
                s1, s2 = words[i][:j], words[i][j:]
                rs1, rs2 = s1[::-1], s2[::-1]
                if isPalindrome(s2) and rs1 in wordIdx and wordIdx[rs1]!=i:
                    ret.append([i, wordIdx[rs1]])
                if isPalindrome(s1) and rs2 in wordIdx and wordIdx[rs2]!=i:
                    ret.append([wordIdx[rs2], i])
        return ret
