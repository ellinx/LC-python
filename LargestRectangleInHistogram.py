"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].




The largest rectangle is shown in the shaded area, which has area = 10 unit.



Example:

Input: [2,1,5,6,2,3]
Output: 10
"""
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 1) Create an empty stack.
        # 2) Start from first bar, and do following for every bar ‘hist[i]’ where ‘i’ varies from 0 to n-1.
        # ……a) If stack is empty or hist[i] is higher than the bar at top of stack, then push ‘i’ to stack.
        # ……b) If this bar is smaller than the top of stack, then keep removing the top of stack while top of the stack is greater. Let the removed bar be hist[tp]. Calculate area of rectangle with hist[tp] as smallest bar. For hist[tp], the ‘left index’ is previous (previous to tp) item in stack and ‘right index’ is ‘i’ (current index).
        # 3) If the stack is not empty, then one by one remove all bars from stack and do step 2.b for every removed bar.
        ret = 0
        if not len(heights):
            return ret
        stk = collections.deque()
        for i in range(len(heights)):
            if len(stk) and heights[i]<heights[stk[-1]]:
                while len(stk) and heights[stk[-1]]>heights[i]:
                    removed = stk.pop()
                    if len(stk):
                        ret = max(ret, heights[removed]*(i-stk[-1]-1))
                    else:
                        ret = max(ret, heights[removed]*(i))
            stk.append(i)
        while len(stk):
            removed = stk.pop()
            if len(stk):
                ret = max(ret, heights[removed]*(len(heights)-stk[-1]-1))
            else:
                ret = max(ret, heights[removed]*(len(heights)))
        return ret
