"""
There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

||||||||||||||
\\|//|\\//\\||

After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R',
if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state.

Example 1:
Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."

Example 2:
Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Note:
1. 0 <= N <= 10^5
2. String dominoes contains only 'L', 'R' and '.'
"""
class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        ret = ""
        l = 0
        while l<len(dominoes):
            while l<len(dominoes) and dominoes[l]=='L':
                l += 1
                ret += "L"
            if l==len(dominoes):
                return ret
            r = l+1
            while r<len(dominoes) and dominoes[r]=='.':
                r += 1
            #print(l,r)
            if r==len(dominoes):
                if dominoes[l]=='.':
                    ret += "."*(r-l)
                else:
                    ret += "R"*(r-l)
                return ret
            if dominoes[r]=='L':
                if (l==0 or dominoes[l-1]=='L' )and dominoes[l]=='.':
                    ret += "L"*(r-l+1)
                else:
                    if (r-l+1)%2==1:
                        m = 1
                    else:
                        m = 0
                    half = (r-l+1)//2
                    #print(ret, half, m)
                    ret += "R"*half+"."*m+"L"*half
                l = r+1
            else:
                if dominoes[l]=='.':
                    ret += "."*(r-l)
                else:
                    ret += "R"*(r-l)
                l = r
            #print(ret)

        return ret
