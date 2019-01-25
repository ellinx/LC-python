"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.

"""
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        ret = strs[0]
        for i in range(1,len(strs)):
            i1, i2 = 0, 0
            while i1<len(ret) and i2<len(strs[i]):
                if ret[i1]==strs[i][i2]:
                    i1 += 1
                    i2 += 1
                    continue
                break
            ret = ret[:i1]
            if len(ret)==0:
                return ret
        return ret
