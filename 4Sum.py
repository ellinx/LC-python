
class FourSum:
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

    """
    Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that 
    A[i] + B[j] + C[k] + D[l] is zero.

    To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the 
    range of -228 to 228 - 1 and the result is guaranteed to be at most 2^31 - 1.

    Example:
    
    Input:
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    
    Output:
    2
    
    Explanation:
    The two tuples are:
    1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
    2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
    """
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        map = {}
        res = 0

        for a in A:
            for b in B:
                sum = a+b
                if sum in map:
                    map[sum] += 1
                else:
                    map[sum] = 1

        for c in C:
            for d in D:
                sum = c+d
                if -sum in map:
                    res += map[-sum]

        return res


# test
if __name__=="__main__":
    tmp = FourSum()
    nums = [1, 0, -1, 0, -2, 2]
    result1 = tmp.fourSum(nums,0)
    for each in result1:
        print(each)

    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    result2 = tmp.fourSumCount(A,B,C,D)
    print(result2)