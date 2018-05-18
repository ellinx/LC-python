"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all
unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class FourSum:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        if n < 4:
            return res

        nums.sort()
        print(nums)
        for i in range(n-3):
            if i>0 and nums[i-1]==nums[i]:
                continue
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target:
                break
            if nums[n-4]+nums[n-3]+nums[n-2]+nums[n-1] < target:
                break

            for j in range(i+1,n-2):
                if j > i+1 and nums[j - 1] == nums[j]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[n - 4] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                    break

                left = j+1
                right = n-1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
                    else:
                        tmp = [nums[i], nums[j], nums[left], nums[right]]
                        res.append(tmp)
                        while True:
                            left += 1
                            if left>=right or nums[left-1]!=nums[left]:
                                break
                        while True:
                            right -= 1
                            if left>=right or nums[right]!=nums[right+1]:
                                break

        return res


# test
if __name__=="__main__":
    tmp = FourSum()
    nums = [1, 0, -1, 0, -2, 2]
    result1 = tmp.fourSum(nums,0)
    for each in result1:
        print(each)
