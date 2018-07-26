"""
Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer from [0, N) which is NOT in B.

Optimize it such that it minimizes the call to system’s Math.random().

Note:

1. 1 <= N <= 1000000000
2. 0 <= B.length < min(100000, N)
3. [0, N) does NOT include N. See interval notation.

Example 1:

Input:
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
Output: [null,0,0,0]

Example 2:

Input:
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
Output: [null,1,1,1]

Example 3:

Input:
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]

Example 4:

Input:
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, N and the blacklist B. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.

"""
class Solution:

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.N = N
        self.list = []
        cur = 0
        for i in sorted(blacklist):
            if cur==i:
                cur += 1
                continue
            if len(self.list)==0:
                self.list.append([i-cur, cur, i-1])
            else:
                self.list.append([self.list[-1][0]+i-cur, cur, i-1])
            cur = i+1
        if cur<N:
            if len(self.list)==0:
                self.list.append([N-cur, cur, N-1])
            else:
                self.list.append([self.list[-1][0]+N-cur, cur, N-1])
        #print(self.list)

    def pick(self):
        """
        :rtype: int
        """
        index = random.randrange(self.list[-1][0])
        #print(index)
        start, end = 0, len(self.list)-1
        while start<=end:
            mid = start+(end-start)//2
            if self.list[mid][0]==index:
                start = mid+1
                break
            if self.list[mid][0]<index:
                start = mid + 1
            else:
                if mid and self.list[mid-1][0]>index:
                    end = mid-1
                else:
                    start = mid
                    break
        return random.randrange(self.list[start][1],self.list[start][2]+1)


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
