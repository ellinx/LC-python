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
        ret = "#"
        for i in range(1,6,2):
            ori = color[i:i+2]
            cur = color[i]*2
            if color[i]=='0':
                pre = "ff"
            else:
                pre = hex(int(color[i],16)-1)[2]*2
            if color[i]=='f':
                nxt = "00"
            else:
                nxt = hex(int(color[i],16)+1)[2]*2
            #print(pre, cur, nxt)
            res = pre
            if abs(int(cur,16)-int(ori,16))<abs(int(res,16)-int(ori,16)):
                res = cur
            if abs(int(nxt,16)-int(ori,16))<abs(int(res,16)-int(ori,16)):
                res = nxt
            ret += res
        return ret
