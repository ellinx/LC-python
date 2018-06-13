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
        def StrStartFromA(s):
            diff = ord(s[0])-ord('a')
            if diff==0:
                return s
            ret = ""
            for c in s:
                temp = ord(c)-diff-ord('a')
                if temp<0:
                    temp += 26
                temp %= 26
                ret += chr(ord('a')+temp)
            return ret

        patternLengthMap = dict()
        for s in strings:
            key = len(s)
            if key not in patternLengthMap:
                patternLengthMap[key] = collections.defaultdict(list)
            #print(s, StrStartFromA(s))
            patternLengthMap[key][StrStartFromA(s)].append(s)
        ret = []
        for k1 in patternLengthMap:
            for k2 in patternLengthMap[k1]:
                ret.append(patternLengthMap[k1][k2])
        return ret
