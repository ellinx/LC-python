"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

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
        def helper(s, cur):
            total = 0
            while cur>=0:
                if s[cur]=='#':
                    total += 1
                    cur -= 1
                    continue
                if total>0:
                    total -= 1
                    cur -= 1
                    continue
                return cur
            return cur

        i1, i2 = helper(S, len(S)-1), helper(T, len(T)-1)
        while i1>=0 and i2>=0:
            if S[i1]!=T[i2]:
                return False
            i1 = helper(S, i1-1)
            i2 = helper(T, i2-1)
        if i1>=0 or i2>=0:
            return False
        return True
