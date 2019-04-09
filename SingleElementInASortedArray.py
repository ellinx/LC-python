"""
Given a sorted array consisting of only integers
where every element appears twice except for one element which appears once.

Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10

Note: Your solution should run in O(log n) time and O(1) space.
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            m = l+(r-l)//2
            #print(l,r,m)
            if (m==l or nums[m-1]!=nums[m]) and (m==r or nums[m+1]!=nums[m]):
                return nums[m]
            if m%2==0:
                if m>0 and nums[m-1]==nums[m]:
                    r = m-2
                else:
                    l = m+2
            else:
                if m>0 and nums[m-1]==nums[m]:
                    l = m+1
                else:
                    r = m-1
        return nums[l]
