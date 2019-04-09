"""
Given a sorted array of integers nums and integer values a, b and c.
Apply a quadratic function of the form f(x) = ax^2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example 1:
Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]

Example 2:
Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
"""
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        if a==0 and b==0:
            return [c]*len(nums)
        if a==0:
            if b>0:
                return list(map(lambda x:a*x*x+b*x+c,nums))
            return list(map(lambda x:a*x*x+b*x+c,nums))[::-1]
        target = -b/(2*a)
        idx = bisect.bisect_left(nums, target)
        print(idx)
        i1, i2 = idx-1,idx
        ret = []
        while i1>=0 and i2<len(nums):
            if (target-nums[i1]<=nums[i2]-target):
                ret.append(a*nums[i1]*nums[i1]+b*nums[i1]+c)
                i1 -= 1
            else:
                ret.append(a*nums[i2]*nums[i2]+b*nums[i2]+c)
                i2 += 1
        while i1>=0:
            ret.append(a*nums[i1]*nums[i1]+b*nums[i1]+c)
            i1 -= 1
        while i2<len(nums):
            ret.append(a*nums[i2]*nums[i2]+b*nums[i2]+c)
            i2 += 1
        if a>0:
            return ret
        return ret[::-1]
