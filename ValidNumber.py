"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous.
You should gather all requirements up front before implementing one.
"""
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        dotIndex, eIndex = -1, -1
        index = 0
        if index<len(s) and s[index] in "+-":
            index += 1
        if index==len(s):
            return False
        while index<len(s):
            if s[index]=='e':
                if eIndex!=-1:
                    return False
                eIndex = index
                if eIndex-1>=0 and (s[eIndex-1]=='.' or s[eIndex-1].isdigit()):
                    index += 1
                    if index==len(s):
                        return False
                    if s[index] in "+-":
                        index += 1
                        if index==len(s):
                            return False
                else:
                    return False
            elif s[index]=='.':
                if dotIndex!=-1 or eIndex!=-1:
                    return False
                dotIndex = index
                index += 1
                if (dotIndex-1>=0 and s[dotIndex-1].isdigit()) or (dotIndex+1<len(s) and s[dotIndex+1].isdigit()):
                    continue
                return False
            else:
                end = index
                while end<len(s) and s[end].isdigit():
                    end += 1
                numStr = s[index:end]
                if len(numStr)==0:
                    return False
                index = end
        return True
