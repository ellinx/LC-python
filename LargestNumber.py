"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:
Input: [10,2]
Output: "210"

Example 2:
Input: [3,30,34,5,9]
Output: "9534330"

Note: The result may be very large, so you need to return a string instead of an integer.
"""
import functools

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def mycmp(x,y):
            if x+y==y+x:
                return 0
            if x+y<y+x:
                return -1
            return 1

        numStr = [str(num) for num in nums]
        numStr.sort(key=functools.cmp_to_key(mycmp), reverse=True)
        ret = ""
        for each in numStr:
            if len(ret)==0 and each=="0":
                continue
            ret += each
        if len(ret)==0:
            return "0"
        return ret
