"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""


class FindAllDuplicatesInArray:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i]-1]:
                tmp = nums[i]
                nums[i], nums[tmp-1] = nums[tmp-1], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(nums[i])

        return res


class Solution2:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        for k,v in collections.Counter(nums).most_common():
            if v==1:
                break
            ret.append(k)
        return ret

class Solution3:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        for num in nums:
            idx = abs(num)-1
            if nums[idx]<0:
                ret.append(abs(num))
            else:
                nums[idx] *= -1
        return ret

# test
if __name__=="__main__":
    tmp = FindAllDuplicatesInArray()
    nums = [4,3,2,7,8,2,3,1]
    result = tmp.findDuplicates(nums)
    print(result)
