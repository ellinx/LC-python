"""
Given an array of scores that are non-negative integers.
Player 1 picks one of the numbers from either end of the array followed by the player 2 and
then player 1 and so on. Each time a player picks a number,
that number will not be available for the next player.
This continues until all the scores have been chosen.
The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner.
You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5,
then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return False.

Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7.
No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12),
so you need to return True representing player1 can win.

Note:
1. 1 <= length of the array <= 20.
2. Any scores in the given array are non-negative integers and will not exceed 10,000,000.
3. If the scores of both players are equal, then player 1 is still the winner.
"""
class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for i in range(1,n):
            r, c = 0, i
            while c<n:
                dp[r][c] = max(nums[r]-dp[r+1][c], nums[c]-dp[r][c-1])
                r, c = r+1, c+1
        #print(dp)
        return dp[0][n-1]>=0

class Solution2:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(nums, mm):
            if len(nums)==0:
                return 0
            key = ",".join(nums)
            if key in mm:
                return mm[key]
            l = int(nums[0])-dfs(nums[1:], mm)
            r = int(nums[-1])-dfs(nums[:-1], mm)
            mm[key] = max(l,r)
            #print(mm)
            return mm[key]

        return dfs([str(num) for num in nums], dict())>=0

class Solution3:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def helper(nums, l, r, mm):
            if l==r:
                return nums[l]
            key = str(l)+","+str(r)
            if key in mm:
                return mm[key]
            pl = nums[l]+sum(nums[l+1:r+1])-helper(nums,l+1,r,mm)
            pr = nums[r]+sum(nums[l:r])-helper(nums,l,r-1,mm)
            mm[key] = max(pl,pr)
            return mm[key]

        p1 = helper(nums, 0, len(nums)-1, dict())
        return p1>=sum(nums)-p1
