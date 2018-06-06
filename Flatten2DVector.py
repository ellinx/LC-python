"""
Implement an iterator to flatten a 2d vector.

Example:

Input: 2d vector =
[
  [1,2],
  [3],
  [4,5,6]
]
Output: [1,2,3,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,2,3,4,5,6].

Follow up:
As an added challenge, try to code it using only iterators in C++ or iterators in Java.

"""
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.row = 0
        self.col = 0
        self.twoD = vec2d

    def next(self):
        """
        :rtype: int
        """
        ret = self.twoD[self.row][self.col]
        if self.col+1==len(self.twoD[self.row]):
            self.row += 1
            self.col = 0
        else:
            self.col += 1
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.col==0:
            while self.row<len(self.twoD) and len(self.twoD[self.row])==0:
                self.row += 1
        if self.row<len(self.twoD) and self.col<len(self.twoD[self.row]):
            return True
        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
