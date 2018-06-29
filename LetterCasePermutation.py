"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]

Note:

1. S will be a string with length at most 12.
2. S will consist only of letters or digits.

"""
class Solution:
    """
    Thoughts:
    1. iteration
    2. for each character, either upper or lower

    Time: O(2^n) where n is length of S
    Space: O(2^n)
    """
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ret = [""]
        for c in S:
            if c.isdigit():
                ret = [each+c for each in ret]
                continue
            ret = [each+c.upper() for each in ret]+[each+c.lower() for each in ret]
        return ret
