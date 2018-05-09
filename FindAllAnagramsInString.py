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
        res = []
        if len(s) < len(p):
            return res
        letters = [0]*26
        count = 0
        for a in p:
            index = ord(a)-ord('a')
            if letters[index] == 0:
                count += 1
            letters[index] += 1

        start, end = 0, 0
        while end < len(p):
            index = ord(s[end])-ord('a')
            if letters[index] == 1:
                count -= 1
            letters[index] -= 1
            end += 1

        end -= 1
        while end < len(s):
            if count == 0:
                res.append(start)

            index = ord(s[start])-ord('a')
            if letters[index] == 0:
                count += 1
            letters[index] += 1
            start += 1
            end += 1
            if (end == len(s)):
                break
            index = ord(s[end])-ord('a')
            if letters[index] == 1:
                count -= 1
            letters[index] -= 1

        return res


# test
if __name__=="__main__":
    test = FindAllAnagramsInString()
    result = test.findAnagrams("abab","ab")
    print(result)