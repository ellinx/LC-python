"""
Given a list of words (without duplicates),
please write a program that returns all concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of
at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation:
"catsdogcats" can be concatenated by "cats", "dog" and "cats";
"dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Note:
1. The number of elements of the given array will not exceed 10,000
2. The length sum of elements in the given array will not exceed 600,000.
3. All the input string will only include lower case letters.
4. The returned elements order does not matter.
"""
class Solution:
    def findAllConcatenatedWordsInADict(self, words: 'List[str]') -> 'List[str]':
        def dfs(word, start, wordSet, mm):
            key = word[start:]
            if start>0:
                if key in wordSet:
                    return True
            if key in mm:
                return mm[key]
            for i in range(start+1,len(word)):
                if word[start:i] not in wordSet:
                    continue
                if dfs(word, i, wordSet, mm):
                    mm[key] = True
                    return True
            mm[key] = False
            return False

        wordSet = set(words)
        ret = []
        mm = dict()
        for word in words:
            if dfs(word, 0, wordSet, mm):
                ret.append(word)
        return ret
