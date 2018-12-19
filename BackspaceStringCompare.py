"""
Given two strings S and T, return if they are equal when both are typed into empty text editors.
# means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:

    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.

Follow up:

    Can you solve it in O(N) time and O(1) space?


"""
class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def getStr(s):
            stk = collections.deque()
            for c in s:
                if c=="#":
                    if len(stk)!=0:
                        stk.pop()
                    continue
                stk.append(c)
            return "".join(stk)

        return getStr(S)==getStr(T)

class Solution2:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def helper(s):
            ret = ""
            b = 0
            for c in s[::-1]:
                if c=='#':
                    b += 1
                else:
                    if b==0:
                        ret = c+ret
                    else:
                        b -= 1
            return ret

        return helper(S)==helper(T)
