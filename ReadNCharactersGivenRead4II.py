"""
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.

Example 1:

Given buf = "abc"
read("abc", 1) // returns "a"
read("abc", 2); // returns "bc"
read("abc", 1); // returns ""

Example 2:

Given buf = "abc"
read("abc", 4) // returns "abc"
read("abc", 1); // returns ""
"""
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.temp = [""]*4
        self.start = 0
        self.validNum = 0

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        index = 0
        if n<=self.validNum:
            for i in range(n):
                buf[index+i] = self.temp[self.start+i]
            self.start += n
            self.validNum -= n
            return n
        for i in range(self.validNum):
            buf[index] = self.temp[self.start+i]
            index += 1
        self.start = 0
        self.validNum = 0
        rlength = 4
        while index<n and rlength==4:
            rlength = read4(self.temp)
            self.validNum = rlength
            for i in range(rlength):
                buf[index] = self.temp[self.start]
                index += 1
                self.start += 1
                self.start %= 4
                self.validNum -= 1
                if index==n:
                    break
        return min(index,n)
