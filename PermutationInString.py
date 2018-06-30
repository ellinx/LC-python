"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:

1. The input strings only contain lower case letters.
2. The length of both given strings is in range [1, 10,000].

"""
class Solution:
    """
    Thoughts:
    1. similar to sliding window

    Time: O(m+n) where m,n is length of s1,s2
    Space: O(n)
    """
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        counter = collections.Counter(s1)
        total = len(s1)
        start, end = 0, 0
        while end<len(s2):
            if s2[end] not in counter:
                end += 1
                continue
            if counter[s2[end]]>0:
                total -= 1
            counter[s2[end]] -= 1
            while total==0:
                if end-start+1==len(s1):
                    return True
                if s2[start] in counter:
                    if counter[s2[start]]>=0:
                        total += 1
                    counter[s2[start]] += 1
                start += 1
            end += 1
        return False
