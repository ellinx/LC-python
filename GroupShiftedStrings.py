"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"

Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]


"""
class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        def helper(s):
            if len(s)==0:
                return ""
            ret = "a"
            dist = ord(s[0])-ord('a')
            for i in range(1,len(s)):
                tmp = ord(s[i])-dist
                if tmp<ord('a'):
                    tmp = ord('z')+1-(ord('a')-tmp)
                elif tmp>ord('z'):
                    tmp = ord('a')-1+tmp-ord('z')
                ret += chr(tmp)
            return ret

        mm = collections.defaultdict(list)
        for s in strings:
            k = helper(s)
            mm[k].append(s)
        ret = []
        for k in mm:
            ret.append(mm[k])
        return ret
