"""
You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.

Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3
3, 4, 5
Example 2:
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3, 4, 5
3, 4, 5
Example 3:
Input: [1,2,3,4,4,5]
Output: False
Note:
The length of the input is in range of [1, 10000]
"""
class SplitArrayIntoConsecutiveSubsequences:
    # when get a number, either append to a sequence ends at number-1, or construct a new sequence starting from number
    # otherwise return False
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = collections.Counter(nums)
        end = collections.defaultdict(int)
        for num in nums:
            if count[num]:
                count[num] -= 1
                if end[num-1]:
                    #append to a sequence ends at num-1
                    end[num-1] -= 1
                    end[num] += 1
                else:
                    #construct a new sequence
                    if count[num+1] and count[num+2]:
                        count[num+1] -= 1
                        count[num+2] -= 1
                        end[num+2] += 1
                    else:
                        return False
        return True
