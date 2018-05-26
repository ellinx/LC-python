import collections
"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


class FindAllAnagramsInString:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ret = []
        if len(s)<len(p):
            return ret
        count = collections.Counter(p)
        total = len(p)
        start, end = 0, 0
        while end<len(s):
            while end<len(s) and end-start<len(p):
                if s[end] in count:
                    count[s[end]] -= 1
                    if count[s[end]]>=0:
                        total -= 1
                end += 1
            #print(start,end,total,count)
            if end-start==len(p):
                if total==0:
                    ret.append(start)
                if s[start] in count:
                    count[s[start]] += 1
                    if count[s[start]]>0:
                        total += 1
                start += 1
            else:
                break
        return ret


# test
if __name__=="__main__":
    test = FindAllAnagramsInString()
    result = test.findAnagrams("abab","ab")
    print(result)
