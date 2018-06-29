"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
class Solution:
    """
    Thoughts:
    1. dp[i] stands for s[0:i] is breakable or not

    Time: O(n*m) where n is length of s and m is length of wordDict
    Space: O(n)
    """
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(s)+1):
            for each in wordDict:
                if i-len(each)>=0 and dp[i-len(each)] and each==s[i-len(each):i]:
                    dp[i] = True
                    break
        return dp[-1]
