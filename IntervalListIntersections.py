"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that is either empty,
or can be represented as a closed interval.

For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:


A   ------         ----------------         ------------------------------  ----

B      ------------         -------------         ---------------------------   ---

ans    ---         -        -------               ------------------------  -  -

    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26


Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.


Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        starts = sorted([each[0] for each in A+B])
        ends = sorted([each[1] for each in A+B])
        #print(starts, ends)
        i, j = 0, 0
        total = 0
        ret = []
        l, r = -1, -1
        while i<len(starts) and j<len(ends):
            if starts[i]<=ends[j]:
                total += 1
                if total==2:
                    l = starts[i]
                i += 1
            else:
                total -= 1
                if total==1:
                    r = ends[j]
                    ret.append([l,r])
                j += 1
        if total==2 and j<len(ends):
            ret.append([l,ends[j]])
        return ret
