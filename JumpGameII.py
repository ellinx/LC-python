"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:
You can assume that you can always reach the last index.
"""
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step = 0
        start, end = 0, 0
        while start<len(nums)-1:
            maxend = end+1
            for i in range(start,end+1):
                if i+nums[i]>=len(nums)-1:
                    return step+1
                maxend = max(maxend, i+nums[i])
            step += 1
            start, end = end+1, maxend
        return step


class Solution2:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==1:
            return 0
        visited = [False]*n
        pq = [[0,0]]
        visited[0] = True
        while len(pq):
            # negative idx
            step, idx = heapq.heappop(pq)
            for each in range(1,nums[-idx]+1):
                nxt = -idx+each
                if nxt>=n:
                    break
                if visited[nxt]:
                    continue
                if nxt==n-1:
                    return step+1
                visited[nxt] = True
                heapq.heappush(pq, [step+1, -nxt])
        return -1
