"""
An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.

The ith edge connects nodes edges[i][0] and edges[i][1] together.

Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

Example 1:

Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation:
Here is a diagram of the given tree:
  0
 / \
1   2
   /|\
  3 4 5
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.

Note: 1 <= N <= 10000
"""
class Solution:
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def dfs1(cur, visited, subNodeNum, subSum):
            visited[cur] = True
            for each in g[cur]:
                if not visited[each]:
                    dfs1(each, visited, subNodeNum, subSum)
                    # adds up all its children subtree
                    subNodeNum[cur] += subNodeNum[each]
                    # total sum of this subtree and use edge cur-each subNodeNum[each] times
                    subSum[cur] += subSum[each]+subNodeNum[each]
            # add node itself
            subNodeNum[cur] += 1

        def dfs2(cur, visited, subNodeNum, subSum):
            visited[cur] = True
            for each in g[cur]:
                if not visited[each]:
                    # all nodes in subtree[each] dist-1, all other nodes dist+1
                    subSum[each] = subSum[cur] - subNodeNum[each] + N - subNodeNum[each]
                    dfs2(each, visited, subNodeNum, subSum)

        # treat node 0 as the root of this tree
        # subNodeNum[i] is total node number of subtree[i], including i
        # subSum[i] is total distance sum of subtree[i]
        g = collections.defaultdict(set)
        for edge in edges:
            g[edge[0]].add(edge[1])
            g[edge[1]].add(edge[0])
        subNodeNum, subSum = [0]*N, [0]*N
        dfs1(0, [False]*N, subNodeNum, subSum)
        #print(subNodeNum,subSum)
        dfs2(0, [False]*N, subNodeNum, subSum)
        return subSum
