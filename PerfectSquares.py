"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


"""
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = collections.deque()
        visited = [False]*(n+1)
        q.append(n)
        visited[n] = True
        level = 0
        while len(q):
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                for i in range(1,cur):
                    nxt = cur-i**2
                    if nxt==0:
                        return level+1
                    if nxt>0:
                        if not visited[nxt]:
                            q.append(nxt)
                            visited[nxt] = True
                    else:
                        break
            level += 1
        return n

        # TLE for python
        def numSquaresDP(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i] is least number of perfect square numbers sum to i
        dp = [0]*(n+1)
        for i in range(1,n+1):
            j = 1
            pre = i-j**2
            while pre>=0:
                if dp[i]==0:
                    dp[i] = dp[pre]+1
                else:
                    dp[i] = min(dp[i],dp[pre]+1)
                j += 1
                pre = i-j**2
        return dp[n]
