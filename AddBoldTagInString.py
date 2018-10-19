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
        li = []
        for word in dict:
            length = len(word)
            start = 0
            while s.find(word, start)!=-1:
                l = s.find(word, start)
                r = l+length-1
                li.append([l,r])
                start = l+1
        if len(li)==0:
            return s
        li.sort()
        #print(li)
        merged = []
        cur = li[0]
        for i in range(1,len(li)):
            if li[i][0]>cur[1]+1:
                merged.append(cur)
                cur = li[i]
                continue
            cur[1] = max(cur[1], li[i][1])
        merged.append(cur)
        #print(merged)
        ret = ""
        idx = 0
        for each in merged:
            ret += s[idx:each[0]]
            ret += "<b>"+s[each[0]:each[1]+1]+"</b>"
            idx = each[1]+1
        ret += s[idx:]
        return ret
