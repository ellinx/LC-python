"""
In the following, every capital letter represents some hexadecimal digit from 0 to f.

The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.
For example, "#15c" is shorthand for the color "#1155cc".

Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" is -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.

Given the color "#ABCDEF", return a 7 character color that is most similar to #ABCDEF,
and has a shorthand (that is, it can be represented as some "#XYZ"

Example 1:
Input: color = "#09f166"
Output: "#11ee66"
Explanation:
The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
This is the highest among any shorthand color.

Note:

1. color is a string of length 7.
2. color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0 to f
3. Any answer which has the same (highest) similarity as the best answer will be accepted.
4. All inputs and outputs should use lowercase letters, and the output is 7 characters.


"""
class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        def helper(s):
            ret = s[0]*2
            if s[0]=='0':
                ls = 'ff'
            else:
                ls = hex(int(s[0],16)-1)[2:]*2
            if abs(int(ls,16)-int(s,16))<abs(int(ret,16)-int(s,16)):
                ret = ls
            if s[0]=='f':
                rs = '00'
            else:
                rs = hex(int(s[0],16)+1)[2:]*2
            if abs(int(rs,16)-int(s,16))<abs(int(ret,16)-int(s,16)):
                ret = rs
            return ret


        ret = "#"
        for i in range(1,6,2):
            ret += helper(color[i:i+2])
        return ret
