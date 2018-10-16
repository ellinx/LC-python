"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
1. All inputs will be in lowercase.
2. The order of your output does not matter.
"""
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mm = dict()
        for each in strs:
            key = "".join(sorted(each))
            if key not in mm:
                mm[key] = list()
            mm[key].append(each)
        return [mm[k] for k in mm]
