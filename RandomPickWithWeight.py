"""
Given an array w of positive integers, where w[i] describes the weight of index i,
write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1. 1 <= w.length <= 10000
2. 1 <= w[i] <= 10^5
3. pickIndex will be called at most 10000 times.

Example 1:

Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]

Example 2:

Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments.
Solution's constructor has one argument, the array w. pickIndex has no arguments.
Arguments are always wrapped with a list, even if there aren't any.

"""
class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.list = [w[0]]*len(w)
        for i in range(1,len(w)):
            self.list[i] = self.list[i-1]+w[i]

    def pickIndex(self):
        """
        :rtype: int
        """
        val = random.randrange(self.list[-1])
        start, end = 0, len(self.list)-1
        while start<=end:
            mid = start+(end-start)//2
            if self.list[mid]==val:
                return mid+1
            if self.list[mid]<val:
                start = mid+1
            else:
                if mid==0 or self.list[mid-1]<=val:
                    return mid
                end = mid-1
        return -1

class Solution2:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.list = []
        total = -1
        for each in w:
            total += each
            self.list.append(total)

    def pickIndex(self):
        """
        :rtype: int
        """
        val = random.randrange(self.list[-1]+1)
        idx = bisect.bisect_left(self.list, val)
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
