"""
X is a good number if after rotating each digit individually by 180 degrees,
we get a valid number that is different from X.
Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves;
2 and 5 rotate to each other; 6 and 9 rotate to each other,
and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Note:

    N  will be in range [1, 10000].


"""
class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        def rotate(s):
            ret = ""
            for c in s:
                if c=='0' or c=='1' or c=='8':
                    ret += c
                elif c=='2':
                    ret += "5"
                elif c=='5':
                    ret += '2'
                elif c=='6':
                    ret += "9"
                elif c=='9':
                    ret += '6'
            return ret

        def dfs(s, cur, strN, ret):
            if len(cur)==len(strN):
                if rotate(cur)!=cur:
                    ret.append(cur)
                return
            for c in s:
                length = len(cur)+1
                if int(cur+c)<=int(strN):
                    dfs(s, cur+c, strN, ret)

        ret = []
        nums = "0182569"
        dfs(nums, "", str(N), ret)
        return len(ret)
