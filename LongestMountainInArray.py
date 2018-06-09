"""
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

    B.length >= 3
    There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]

(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.

Note:

    0 <= A.length <= 10000
    0 <= A[i] <= 10000

Follow up:

    Can you solve it using only one pass?
    Can you solve it in O(1) space?


"""
class Solution:
    #loop once and find all mountains
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ret = 0
        if len(A)<3:
            return ret
        start, end = 0, 1
        while end<len(A):
            if A[end]<=A[start]:
                start = end
                end += 1
            else:
                peak = end+1
                while peak<len(A) and A[peak]>A[peak-1]:
                    peak += 1
                peak -= 1
                end = peak+1
                while end<len(A) and A[end]<A[end-1]:
                    end += 1
                end -= 1
                if end==peak:
                    start = end
                    end += 1
                    continue
                ret = max(ret, end-start+1)
                start = end
                end += 1
        return ret

    # find peak and then find mountain
    def longestMountain2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        peaks = []
        for i in range(1,len(A)-1):
            if A[i]>A[i-1] and A[i]>A[i+1]:
                peaks.append(i)
        ret = 0
        for index in peaks:
            start,end = index-1,index+1
            while start>=0:
                if A[start]<A[start+1]:
                    start -= 1
                else:
                    break
            start += 1
            while end<len(A):
                if A[end]<A[end-1]:
                    end += 1
                else:
                    break
            end -= 1
            #print(start,end)
            ret = max(ret, end-start+1)
        return ret
