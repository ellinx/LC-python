"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""

class EvaluateDivision:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        g = collections.defaultdict(dict)
        for i in range(len(equations)):
            g[equations[i][0]][equations[i][1]] = values[i]
            g[equations[i][1]][equations[i][0]] = 1.0/values[i]
        ret = []
        for query in queries:
            if query[0] not in g:
                ret.append(-1.0)
                continue
            if query[0]==query[1]:
                ret.append(1.0)
                continue
            # BFS
            visited = set()
            visited.add(query[0])
            q = collections.deque()
            for k in g[query[0]]:
                visited.add(k)
                q.append((k, g[query[0]][k]))
            while len(q):
                cur = q.popleft()
                if cur[0]==query[1]:
                    ret.append(cur[1])
                    break
                for k in g[cur[0]]:
                    if k not in visited:
                        visited.add(k)
                        q.append((k, cur[1]*g[cur[0]][k]))
            else:
                ret.append(-1.0)
        return ret
