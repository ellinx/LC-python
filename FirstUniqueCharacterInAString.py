"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
class FirstUniqueCharacterInAString:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = collections.Counter(s)
        ret = -1
        for k in counter:
            if counter[k]==1:
                if ret==-1:
                    ret = s.find(k)
                else:
                    ret = min(ret, s.find(k))
        return ret
