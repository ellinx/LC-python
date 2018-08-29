"""
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict.
If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag.
Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

Example 1:
Input:
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"

Example 2:
Input:
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"

Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
"""    
class Solution:
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        # similar like merge intervals
        lengthInDict = set()
        for each in dict:
            lengthInDict.add(len(each))
        bold = []
        cur = None
        for i in range(len(s)):
            for each in lengthInDict:
                if i+each<=len(s) and s[i:i+each] in dict:
                    if cur is None:
                        cur = [i,i+each-1]
                    else:
                        if cur[1]<i-1:
                            bold.append(cur)
                            cur = [i, i+each-1]
                        else:
                            cur[1] = max(cur[1], i+each-1)
        if cur is not None:
            bold.append(cur)
        #print(bold)
        if len(bold)==0:
            return s
        ret = ""
        start = 0
        for each in bold:
            ret += s[start:each[0]]+"<b>"+s[each[0]:each[1]+1]+"</b>"
            start = each[1]+1
        ret += s[start:]
        return ret
