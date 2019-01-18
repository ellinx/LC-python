"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Example 1:
Input: pattern = "abab", str = "redblueredblue"
Output: true

Example 2:
Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
Output: true

Example 3:
Input: pattern = "aabb", str = "xyzabcxzyabc"
Output: false

Notes:
You may assume both pattern and str contains only lowercase letters.

"""
class Solution:
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        def dfs(pattern, start1, s, start2, wordMap, mapped):
            if start1==len(pattern) and start2==len(s):
                return True
            if start1==len(pattern) or start2==len(s):
                return False
            if pattern[start1] in wordMap:
                if wordMap[pattern[start1]]==s[start2:start2+len(wordMap[pattern[start1]])]:
                    if dfs(pattern, start1+1, s, start2+len(wordMap[pattern[start1]]), wordMap, mapped):
                        return True
                return False
            for i in range(start2+1,len(s)+1):
                if s[start2:i] in mapped:
                    continue
                wordMap[pattern[start1]] = s[start2:i]
                mapped.add(s[start2:i])
                if dfs(pattern, start1+1, s, i, wordMap, mapped):
                    return True
                mapped.remove(s[start2:i])
                wordMap.pop(pattern[start1])
            return False

        return dfs(pattern, 0, str, 0, dict(), set())
