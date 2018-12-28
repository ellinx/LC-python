"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK.
Thus, the itinerary must begin with JFK.

Note:

1. If there are multiple valid itineraries, you should return the itinerary
    that has the smallest lexical order when read as a single string.
    For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
2. All airports are represented by three capital letters (IATA code).
3. You may assume all tickets form at least one valid itinerary.

Example 1:
Input: tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
                But it is larger in lexical order.

"""
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def dfs(g, last, cur, total):
            if total==0:
                return cur
            for i in range(len(g[last])):
                if i-1>=0 and g[last][i-1]==g[last][i]:
                    continue
                tmp = g[last][i]
                g[last] = g[last][:i]+g[last][i+1:]
                ret = dfs(g, tmp, cur+[tmp], total-1)
                if ret is not None:
                    return ret
                g[last] = g[last][:i]+[tmp]+g[last][i:]
            return None

        g = collections.defaultdict(list)
        for begin, end in tickets:
            g[begin].append(end)
        for k in g:
            g[k].sort()
        #print(g)
        return dfs(g, "JFK", ["JFK"], len(tickets))
