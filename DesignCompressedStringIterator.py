"""
Design and implement a data structure for a compressed string iterator.
It should support the following operations: next and hasNext.

The given compressed string will be in the form of each letter followed by
a positive integer representing the number of this letter existing in the original uncompressed string.

next() - if the original string still has uncompressed characters, return the next letter;
            Otherwise return a white space.
hasNext() - Judge whether there is any letter needs to be uncompressed.

Example:

StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

iterator.next(); // return 'L'
iterator.next(); // return 'e'
iterator.next(); // return 'e'
iterator.next(); // return 't'
iterator.next(); // return 'C'
iterator.next(); // return 'o'
iterator.next(); // return 'd'
iterator.hasNext(); // return true
iterator.next(); // return 'e'
iterator.hasNext(); // return false
iterator.next(); // return ' '
"""
class StringIterator:

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.s = compressedString
        self.idx = 0
        self.c = ""
        self.count = 0
        self.hasNext()

    def next(self):
        """
        :rtype: str
        """
        #print(self.c, self.count)
        if self.count==0:
            if not self.hasNext():
                return " "
        self.count -= 1
        return self.c

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.count>0:
            return True
        if self.idx>=len(self.s):
            self.count = 0
            return False
        self.c = self.s[self.idx]
        self.idx += 1
        start = self.idx
        while self.idx<len(self.s) and self.s[self.idx].isdigit():
            self.idx += 1
        self.count = int(self.s[start:self.idx])
        return self.count>0

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
