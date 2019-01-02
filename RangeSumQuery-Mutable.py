"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8

Note:

1. The array is only modifiable by the update function.
2. You may assume the number of calls to update and sumRange function is distributed evenly.


"""
class NumArray:

    """
    Thoughts:
    1. Segment tree
    """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        def fillST(st, cur, nums, start, end):
            if start==end:
                st[cur] = nums[start]
                return st[cur]
            mid = start+(end-start)//2
            left = fillST(st, 2*cur, nums, start, mid)
            right = fillST(st, 2*cur+1, nums, mid+1, end)
            st[cur] = left+right
            return st[cur]

        self.nums = nums
        if len(nums):
            self.ST = collections.defaultdict(int)
            fillST(self.ST, 1, nums, 0, len(nums)-1)
            #print(self.ST)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        def helper(st, cur, start, end, nums, i, val):
            if i>=start and i<=end:
                st[cur] += val-nums[i]
            if start==end:
                return
            mid = start+(end-start)//2
            if i<=mid:
                helper(st, 2*cur, start, mid, nums, i, val)
            else:
                helper(st, 2*cur+1, mid+1, end, nums, i, val)

        if len(self.nums):
            helper(self.ST, 1, 0, len(self.nums)-1, self.nums, i, val)
            self.nums[i] = val
            #print(self.ST)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def helper(st, cur, start, end, nums, i, j):
            if start==i and end==j:
                return st[cur]
            mid = start+(end-start)//2
            if j<=mid:
                return helper(st, 2*cur, start, mid, nums, i, j)
            elif i>mid:
                return helper(st, 2*cur+1, mid+1, end, nums, i, j)
            else:
                return helper(st, 2*cur, start, mid, nums, i, mid)+helper(st, 2*cur+1, mid+1, end, nums, mid+1, j)

        return helper(self.ST, 1, 0, len(self.nums)-1, self.nums, i, j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)


class SegmentNode:
    def __init__(self, s, e, val):
        self.start = s
        self.end = e
        self.val = val
        self.left = None
        self.right = None

class NumArray2:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        def createSegmentNode(nums, l, r):
            if l>r:
                return None
            if l==r:
                return SegmentNode(l,r,nums[l])
            m = l+(r-l)//2
            left = createSegmentNode(nums, l, m)
            right = createSegmentNode(nums, m+1, r)
            ret = SegmentNode(l, r, left.val+right.val)
            ret.left, ret.right = left, right
            return ret

        self.root = createSegmentNode(nums, 0, len(nums)-1)
        self.nums = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        cur = self.root
        while True:
            cur.val += val-self.nums[i]
            if cur.start==cur.end:
                break
            mid = cur.start+(cur.end-cur.start)//2
            if i<=mid:
                cur = cur.left
            else:
                cur = cur.right
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def sumFromNode(cur, i, j):
            if cur is None or i>cur.end or j<cur.start:
                return 0
            if i<=cur.start and j>=cur.end:
                return cur.val
            mid = cur.start+(cur.end-cur.start)//2
            if i>mid:
                return sumFromNode(cur.right, i, j)
            elif j<=mid:
                return sumFromNode(cur.left, i, j)
            else:
                return sumFromNode(cur.left, i, mid)+sumFromNode(cur.right, mid+1, j)

        return sumFromNode(self.root, i, j)
