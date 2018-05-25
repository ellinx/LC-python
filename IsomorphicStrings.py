"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.
"""
class IsomorphicStrings:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        replace_map = dict()
        index = 0
        while index<len(s):
            if s[index] not in replace_map:
                if t[index] in replace_map.values():
                    return False
                replace_map[s[index]] = t[index]
                index += 1
                continue
            if replace_map[s[index]] != t[index]:
                return False
            index += 1
        return True
