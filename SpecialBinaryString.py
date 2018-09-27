"""

Special binary strings are binary strings with the following two properties:

The number of 0's is equal to the number of 1's.
Every prefix of the binary string has at least as many 1's as 0's.
Given a special string S, a move consists of choosing two consecutive, non-empty, special substrings of S, and swapping them.
(Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.)

At the end of any number of moves, what is the lexicographically largest resulting string possible?

Example 1:
Input: S = "11011000"
Output: "11100100"
Explanation:
The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.

Note:

1. S has length at most 50.
2. S is guaranteed to be a special binary string as defined above.
"""
class Solution:
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        ss = []
        start, end = 0, 0
        count = 0
        while end<len(S):
            if S[end]=='1':
                count += 1
            else:
                count -= 1
            end += 1
            if count==0:
                ss.append('1'+self.makeLargestSpecial(S[start+1:end-1])+'0')
                start = end
        return "".join(sorted(ss,reverse=True))
