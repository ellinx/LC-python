"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"

"""
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = "1"
        for i in range(1,n):
            nxt = ""
            index = 0
            while index<len(ret):
                end = index+1
                while end<len(ret) and ret[end]==ret[index]:
                    end += 1
                nxt += str(end-index)+ret[index]
                index = end
            ret = nxt
        return ret

class Solution2:
    def countAndSay(self, n: int) -> str:
        def process(s):
            ret = []
            idx, cnt = 0, 0
            while idx<len(s):
                if idx==0:
                    cnt = 1
                    idx += 1
                    continue
                if s[idx-1]!=s[idx]:
                    ret.append(str(cnt)+s[idx-1])
                    cnt = 1
                else:
                    cnt += 1
                idx += 1
            ret.append(str(cnt)+s[idx-1])
            return "".join(ret)

        ret = "1"
        for _ in range(n-1):
            ret = process(ret)
        return ret
