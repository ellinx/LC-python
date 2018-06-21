"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order.
All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

1. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
    For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
2. All airports are represented by three capital letters (IATA code).
3. You may assume all tickets form at least one valid itinerary.

Example 1:

Input: tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:

Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.

"""
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def dfs(g, cur, ticketsLeft):
            #print(ticketsLeft,cur)
            if ticketsLeft==0:
                nonlocal ret
                ret = cur
                return True
            for each in sorted(list(g[cur[-1]])):
                if g[cur[-1]][each]==1:
                    g[cur[-1]].pop(each)
                else:
                    g[cur[-1]][each] -= 1
                if dfs(g, cur+[each],ticketsLeft-1):
                    return True
                if each not in g[cur[-1]]:
                    g[cur[-1]][each] = 0
                g[cur[-1]][each] += 1
            return False

        g = collections.defaultdict(dict)
        for ticket in tickets:
            if ticket[1] not in g[ticket[0]]:
                g[ticket[0]][ticket[1]] = 0
            g[ticket[0]][ticket[1]] += 1
        #print(g)
        ret = []
        dfs(g,["JFK"], len(tickets))
        return ret
