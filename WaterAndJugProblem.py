"""
You are given two jugs with capacities x and y litres.
There is an infinite amount of water supply available.
You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

1. Fill any of the jugs completely with water.
2. Empty any of the jugs.
3. Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.

Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True

Example 2:

Input: x = 2, y = 6, z = 5
Output: False

"""
class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        # treat two jugs as one system
        # BFS
        if z>x+y:
            return False
        if x>y:
            return self.canMeasureWater(y,x,z)
        q = collections.deque()
        visited = set()
        visited.add(0)
        q.append(0)
        while len(q):
            cur = q.popleft()
            if cur<=x:
                nxt = cur+x
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
                nxt = cur+y
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
            elif cur<=y:
                nxt = cur-x
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
                nxt = cur+x
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
            elif cur<=x+y:
                nxt = cur-x
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
                nxt = cur-y
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
            if z in visited:
                return True
        #print(visited)
        return False
