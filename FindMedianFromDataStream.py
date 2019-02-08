"""
Median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

For example,
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
"""
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []
        self.total = 0

    def addNum(self, num: 'int') -> 'None':
        if self.total%2==1:
            heapq.heappush(self.left, -num)
            temp = -heapq.heappop(self.left)
            heapq.heappush(self.right, temp)
        else:
            heapq.heappush(self.right, num)
            temp = heapq.heappop(self.right)
            heapq.heappush(self.left, -temp)
        self.total += 1

    def findMedian(self) -> 'float':
        if self.total%2==1:
            return -self.left[0]
        return (-self.left[0]+self.right[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
