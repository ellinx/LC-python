"""
You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:

Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []
"""
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words)==0:
            return []
        wlength = len(words[0])
        count = collections.Counter(words)
        total = len(words)
        ret = []
        for i in range(len(s)-wlength*len(words)+1):
            seen = collections.defaultdict(int)
            for n in range(len(words)):
                cur = s[i+n*wlength:i+(n+1)*wlength]
                if cur not in count:
                    break
                seen[cur] += 1
                if seen[cur]>count[cur]:
                    break
            else:
                ret.append(i)
        return ret
