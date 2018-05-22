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
class AddBoldTagInString:
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        # similar like merge intervals
        li = []
        for word in dict:
            start = s.find(word)
            while start>=0:
                li.append((start,start+len(word)-1))
                start = s.find(word, start+1)
        if not len(li):
            return s
        heapq.heapify(li)
        #print(li)
        merged = []
        start, end = li[0]
        heapq.heappop(li)
        while len(li):
            if li[0][0]>end+1:
                merged.append((start,end))
                start, end = heapq.heappop(li)
            else:
                end = max(end, li[0][1])
                heapq.heappop(li)
        merged.append((start,end))
        #print(merged)
        pre, ret = 0, ''
        for each in merged:
            ret += s[pre:each[0]]+'<b>'+s[each[0]:each[1]+1]+'</b>'
            pre = each[1]+1
        if pre<len(s):
            ret += s[pre:]
        return ret
