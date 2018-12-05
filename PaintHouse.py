"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green.
The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix.
For example, costs[0][0] is the cost of painting house 0 with color red;
costs[1][2] is the cost of painting house 1 with color green, and so on...
Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
             Minimum cost: 2 + 5 + 3 = 10.


"""
class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs)==0:
            return 0
        cost = costs[0]
        for i in range(1,len(costs)):
            tmp = [0]*3
            tmp[0] = min(cost[1], cost[2])+costs[i][0]
            tmp[1] = min(cost[0], cost[2])+costs[i][1]
            tmp[2] = min(cost[0], cost[1])+costs[i][2]
            cost = tmp
        return min(cost)
