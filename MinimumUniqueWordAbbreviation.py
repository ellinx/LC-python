"""
A string such as "word" contains the following abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

Given a target string and a set of strings in a dictionary,
find an abbreviation of this target string with the smallest possible length such that
it does not conflict with abbreviations of the strings in the dictionary.

Each number or letter in the abbreviation is considered length = 1.
For example, the abbreviation "a32bc" has length = 4.

Note:
1. In the case of multiple answers as shown in the second example below, you may return any one of them.
2. Assume length of target string = m, and dictionary size = n.
    You may assume that m ≤ 21, n ≤ 1000, and log2(n) + m ≤ 20.

Examples:
"apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")

"apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").
"""
class Solution:
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        def dfsAbbr(s, start, cur, count, ret):
            if start==len(s):
                if count:
                    cur[0] += str(count)
                    cur[1] += 1
                ret.append(cur)
                return
            # not abbr current character
            if count:
                dfsAbbr(s, start+1, [cur[0]+str(count)+s[start], cur[1]+2], 0, ret)
            else:
                dfsAbbr(s, start+1, [cur[0]+s[start], cur[1]+1], 0, ret)
            # abbr current character
            dfsAbbr(s, start+1, cur, count+1, ret)

        def checkAbbr(word, abbr):
            i1, i2 = 0, 0
            while i1<len(word) and i2<len(abbr):
                if abbr[i2].isalpha():
                    if word[i1]!=abbr[i2]:
                        return False
                    i1 += 1
                    i2 += 1
                    continue
                end = i2
                while end<len(abbr) and abbr[end].isdigit():
                    end += 1
                i1 += int(abbr[i2:end])
                i2 = end
            if i1==len(word) and i2==len(abbr):
                return True
            return False

        if len(dictionary)==0:
            return str(len(target))
        abbrs = []
        dfsAbbr(target, 0, ["", 0], 0, abbrs)
        abbrs.sort(key=lambda x:x[1])
        #print(abbrs)
        targetLen = len(target)
        dictionary = list(filter(lambda x:len(x)==targetLen,dictionary))
        for abbr,length in abbrs:
            hasSameAbbr = False
            for word in dictionary:
                if not checkAbbr(word, abbr):
                    continue
                hasSameAbbr = True
                break
            if not hasSameAbbr:
                return abbr
        return target
