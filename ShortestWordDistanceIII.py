"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1

Input: word1 = "makes", word2 = "makes"
Output: 3

Note:
You may assume word1 and word2 are both in the list.

"""
class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ret = float('inf')
        i1, i2 = None, None
        for i in range(len(words)):
            if words[i]==word1:
                i1 = i
            if words[i]==word2:
                if word1==word2:
                    i1 = i2
                i2 = i
            if i1 is not None and i2 is not None:
                ret = min(ret, abs(i1-i2))
        return ret
