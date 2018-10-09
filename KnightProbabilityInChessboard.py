"""
On an NxN chessboard, a knight starts at the r-th row and c-th column
and attempts to make exactly K moves. The rows and columns are 0 indexed,
so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below.
Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Each time the knight is to move, it chooses one of eight possible moves uniformly at random
(even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard.
Return the probability that the knight remains on the board after it has stopped moving.

Example:
Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.

Note:
1. N will be between 1 and 25.
2. K will be between 0 and 100.
3. The knight always initially starts on the board.
"""
class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        # back from final state to initial state
        dirs = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]
        cur = [[1]*N for _ in range(N)]
        for _ in range(K):
            pre = [[0]*N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for each in dirs:
                        ni = i+each[0]
                        nj = j+each[1]
                        if ni>=0 and ni<N and nj>=0 and nj<N:
                            pre[i][j] += cur[ni][nj]
            cur = pre
        return cur[r][c]/(8**K)