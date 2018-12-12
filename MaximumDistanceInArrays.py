"""
Given m arrays, and each array is sorted in ascending order.
Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance.
We define the distance between two integers a and b to be their absolute difference |a-b|.
Your task is to find the maximum distance.

Example 1:
Input:
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation:
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

Note:
1. Each given array will have at least 1 number. There will be at least two non-empty arrays.
2. The total number of the integers in all the m arrays will be in the range of [2, 10000].
3. The integers in the m arrays will be in the range of [-10000, 10000].
"""
class Solution:
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        n = len(arrays)
        left = [[arrays[0][-1], arrays[0][0]] for _ in range(n)]
        for i in range(1,n):
            left[i][0] = max(left[i-1][0], arrays[i][-1])
            left[i][1] = min(left[i-1][1], arrays[i][0])
        #print("left", left)
        right = [[arrays[-1][-1], arrays[-1][0]] for _ in range(n)]
        for i in range(n-2,-1,-1):
            right[i][0] = max(right[i+1][0], arrays[i][-1])
            right[i][1] = min(right[i+1][1], arrays[i][0])
        #print("right", right)
        ret = 0
        for i in range(n):
            if i==0:
                ret = max(ret, abs(right[i+1][1]-arrays[i][-1]), abs(right[i+1][0]-arrays[i][0]))
            elif i==n-1:
                ret = max(ret, abs(left[i-1][1]-arrays[i][-1]), abs(left[i-1][0]-arrays[i][0]))
            else:
                omax = max(left[i-1][0], right[i+1][0])
                omin = min(left[i-1][1], right[i+1][1])
                ret = max(ret, abs(omin-arrays[i][-1]), abs(omax-arrays[i][0]))
        return ret
