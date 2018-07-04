"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

"""
class Solution:
    """
    Time: O(n) where n is length of pattern
    Space: O(n)
    """
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        wordMap = dict()
        mapped = set()
        strs = str.split(" ")
        if len(pattern)!=len(strs):
            return False
        for i in range(len(pattern)):
            if pattern[i] in wordMap:
                if wordMap[pattern[i]]==strs[i]:
                    continue;
                else:
                    return False
            if strs[i] in mapped:
                return False
            wordMap[pattern[i]] = strs[i]
            mapped.add(strs[i])
        return True
