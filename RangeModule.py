"""
A Range Module is a module that tracks ranges of numbers.
Your task is to design and implement the following interfaces in an efficient manner.

addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval.
                                Adding an interval that partially overlaps with currently tracked numbers should add any numbers
                                in the interval [left, right) that are not already tracked.
queryRange(int left, int right) Returns true if and only if every real number in the interval [left, right) is currently being tracked.
removeRange(int left, int right) Stops tracking every real number currently being tracked in the interval [left, right).

Example 1:
addRange(10, 20): null
removeRange(14, 16): null
queryRange(10, 14): true (Every number in [10, 14) is being tracked)
queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)

Note:
1. A half open interval [left, right) denotes all real numbers left <= x < right.
2. 0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
3. The total number of calls to addRange in a single test case is at most 1000.
4. The total number of calls to queryRange in a single test case is at most 5000.
5. The total number of calls to removeRange in a single test case is at most 1000.
"""
class RangeModule:

    def __init__(self):
        self.range = []

    def insertIdx(self, left):
        l, r = 0, len(self.range)-1
        while l<=r:
            m = l+(r-l)//2
            if self.range[m][0]==left:
                return m
            if self.range[m][0]<left:
                l = m+1
            else:
                r = m-1
        return l

    def addRange(self, left: int, right: int) -> None:
        idx = self.insertIdx(left)
        self.range.insert(idx,[left,right])
        if idx==0:
            cur = [left,right]
            newRange = []
        else:
            cur = self.range[idx-1]
            newRange = self.range[:idx-1]
        while idx<len(self.range):
            if cur[1]<self.range[idx][0]:
                newRange.append(cur)
                cur = self.range[idx]
                idx += 1
                continue
            cur[1] = max(cur[1], self.range[idx][1])
            idx += 1
        newRange.append(cur)
        self.range = newRange
        #print("add ",left,right,self.range)


    def queryRange(self, left: int, right: int) -> bool:
        idx = self.insertIdx(left)
        if idx==len(self.range):
            if len(self.range)>0 and right<=self.range[-1][1]:
                return True
            return False
        if self.range[idx][0]==left:
            return right<=self.range[idx][1]
        if idx==0:
            return False
        return right<=self.range[idx-1][1]


    def removeRange(self, left: int, right: int) -> None:
        if len(self.range)==0 or right<=self.range[0][0] or left>=self.range[-1][1]:
            #print("remove ",left,right,self.range)
            return
        idx = self.insertIdx(left)
        if idx==0:
            cur = self.range[0]
            idx += 1
            newRange = []
        else:
            cur = self.range[idx-1]
            newRange = self.range[:idx-1]
        if cur[0]>right:
            newRange.append(cur)
            newRange.extend(self.range[idx:])
            self.range = newRange
            #print("remove ",left,right,self.range)
            return
        if cur[0]<left:
            if cur[1]<=left:
                newRange.append(cur)
            else:
                newRange.append([cur[0],left])
        if cur[1]>right:
            newRange.append([right,cur[1]])
            newRange.extend(self.range[idx:])
            self.range = newRange
            #print("remove ",left,right,self.range)
            return
        while idx<len(self.range):
            if self.range[idx][1]<right:
                idx += 1
            else:
                break
        if idx<len(self.range):
            newRange.append([max(self.range[idx][0],right),self.range[idx][1]])
            newRange.extend(self.range[idx+1:])
        self.range = newRange
        #print("remove ",left,right,self.range)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
