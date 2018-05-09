"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""


class MaximumXOROfTwoNumbersInArray(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        mask = 0
        for i in range(31,-1,-1):
            mask |= 1<<i
            numSet = set()
            for num in nums:
                numSet.add(num & mask)

            nextRes = res | (1<<i)
            for num in numSet:
                if (num ^ nextRes) in numSet:
                    res = nextRes
                    break

        return res


# test
if __name__=="__main__":
    tmp = MaximumXOROfTwoNumbersInArray()
    nums = [3, 10, 5, 25, 2, 8]
    result = tmp.findMaximumXOR(nums)
    print(result)
