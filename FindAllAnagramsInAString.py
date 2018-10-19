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


class Solution:
    """
    Thoughts:
    1. similar to sliding window

    Time: O(m+n) where m is length of s and n is length of p
    Space: O(n)
    """
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        counter = collections.Counter(p)
        total = len(p)
        ret = []
        start, end = 0, 0
        while end<len(s):
            if s[end] in counter:
                if counter[s[end]]>0:
                    total -= 1
                counter[s[end]] -=1
            if end-start+1<len(p):
                end += 1
                continue
            if total==0:
                ret.append(start)
            if s[start] in counter:
                if counter[s[start]]>=0:
                    total += 1
                counter[s[start]] +=1
            start += 1
            end += 1
        return ret


# test
if __name__=="__main__":
    test = Solution()
    result = test.findAnagrams("abab","ab")
    print(result)
