"""
 Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid.
 We define the validity of a string by these rules:

1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
5. An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True

Note:
1. The string size will be in the range [1, 100].

"""
class Solution:
    """
    Thoughts:
    1. two stacks, one store index of ( and one store index of *
    2. if we see a ), use one (, otherwise use one * (leftmost one)
    3. if we have unpaired ( in the stack after go through s,
        we need to see if these * is on the rightside of the (. If yes, they are a pair.

    Time: O(n) where n is length of s
    Space: O(n)
    """
    def checkValidString(self, s: str) -> bool:
        left, star = [],[]
        for i,c in enumerate(s):
            #print(i,c,left,star)
            if c=="(":
                left.append(i)
            elif c==")":
                if len(left)==0 and len(star)==0:
                    return False
                if len(left)>0:
                    left.pop()
                else:
                    star.pop(0)
            elif c=="*":
                star.append(i)
        i1, i2 = 0, 0
        while i1<len(left) and i2<len(star):
            if left[i1]<star[i2]:
                i1 += 1
                i2 += 1
            else:
                i2 += 1
        return i1==len(left)
