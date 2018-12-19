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
        self.maxHeap = []
        self.minHeap = []

    # (small half) in max heap and (large half) in min heap
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not len(self.minHeap):
            heapq.heappush(self.minHeap, num)
            return
        if len(self.maxHeap)==len(self.minHeap):
            num = -heapq.heappushpop(self.maxHeap, -num)
            heapq.heappush(self.minHeap, num)
        else:
            num = heapq.heappushpop(self.minHeap, num)
            heapq.heappush(self.maxHeap, -num)
        #print(self.maxHeap, self.minHeap)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeap)<len(self.minHeap):
            return self.minHeap[0]
        return (-self.maxHeap[0]+self.minHeap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
