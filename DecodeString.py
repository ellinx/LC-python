"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""
class Solution:
    def decodeString(self, s: str) -> str:
        ret = ""
        stk = collections.deque()
        repeat = 1
        l, r = 0, 0
        while l<len(s):
            if s[l]=='[':
                stk.append(ret)
                stk.append(repeat)
                ret, repeat = "", 1
                l += 1
            elif s[l]==']':
                repeat = stk.pop()
                ret = stk.pop()+ret*repeat
                l += 1
            elif s[l].isdigit():
                r = l+1
                while s[r].isdigit():
                    r += 1
                repeat = int(s[l:r])
                l = r
            else:
                ret += s[l]
                l += 1
        return ret
