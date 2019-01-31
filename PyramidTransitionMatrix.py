"""
We are stacking blocks to form a pyramid. Each block has a color which is a one letter string, like `'Z'`.

For every block of color `C` we place not in the bottom row,
we are placing it on top of a left block of color `A` and right block of color `B`.
We are allowed to place the block there only if `(A, B, C)` is an allowed triple.

We start with a bottom row of bottom, represented as a single string.
We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:
Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  D   E
 / \ / \
X   Y   Z

This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.

Example 2:
Input: bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.

Note:
1. bottom will be a string with length in range [2, 8].
2. allowed will have length in range [0, 200].
3. Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.
"""
class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        def dfs(bottom, start, cur, mm):
            #print(bottom, start, cur)
            if len(bottom)==1:
                return True
            nxt = ""
            if len(mm[bottom[start-1:start+1]])==0:
                return False
            for each in mm[bottom[start-1:start+1]]:
                if start+1<len(bottom) and dfs(bottom, start+1, cur+each, mm):
                    return True
                if start+1==len(bottom) and dfs(cur+each, 1, "", mm):
                    return True
            return False

        mm = collections.defaultdict(set)
        for each in allowed:
            mm[each[:2]].add(each[2])
        print(mm)
        return dfs(bottom, 1, "", mm)
