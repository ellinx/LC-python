"""
Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

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
    def firstUniqChar(self, s: 'str') -> 'int':
        counter = collections.Counter(s)
        for i in range(len(s)):
            if counter[s[i]]==1:
                return i
        return -1
