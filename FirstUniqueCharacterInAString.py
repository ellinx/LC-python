"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
class Solution:
    """
    Thoughts:
    1. count occurrence of each character in string
    2. check the first unique character

    Time: O(n)
    Space: O(n)
    """
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return -1
        counter = collections.Counter(s)
        if counter.most_common()[-1][1]>1:
            return -1
        for i in range(len(s)):
            if counter[s[i]]==1:
                return i
        return -1
