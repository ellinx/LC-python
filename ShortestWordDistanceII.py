"""
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2
and return the shortest distance between these two words in the list.
Your method will be called repeatedly many times with different parameters.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3

Input: word1 = "makes", word2 = "coding"
Output: 1

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.word_index = collections.defaultdict(list)
        for i in range(len(words)):
            self.word_index[words[i]].append(i)
        #print(self.word_index)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = self.word_index[word1]
        l2 = self.word_index[word2]
        #print(l1)
        #print(l2)
        i1, i2 = 0, 0
        pre = None
        ret = float('inf')
        while i1<len(l1) and i2<len(l2):
            if l1[i1]<l2[i2]:
                if pre and pre[0]==2:
                    ret = min(ret, l1[i1]-pre[1])
                pre = (1, l1[i1])
                i1 += 1
            else:
                if pre and pre[0]==1:
                    ret = min(ret, l2[i2]-pre[1])
                pre = (2, l2[i2])
                i2 += 1
        if i1<len(l1):
            ret = min(ret, l1[i1]-pre[1])
        if i2<len(l2):
            ret = min(ret, l2[i2]-pre[1])
        return ret



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
