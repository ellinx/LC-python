"""
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""

class ArithmeticSlices(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A)<3:
            return 0

        res = 0
        start = 0;
        end = start+2
        step = A[start+1]-A[start]

        while end<len(A):
            if A[end]-A[end-1]==step:
                end += 1
            else:
                if end-start>2:
                    res += self.helper(end-start)
                    start = end-1
                    end = start+2
                    step = A[start+1]-A[start]
                else:
                    start = start+1
                    end = start+2
                    step = A[start+1]-A[start]

        if end-start>2:
            res += self.helper(end-start)

        return res

    def helper(self, num):
        if num<3:
            return 0

        total = 0
        for i in range(3,num+1):
            total += num-1 - (i-1) + 1

        return total


#test
if __name__=="__main__":
    tmp = ArithmeticSlices()
    A = [1,2,3,4]
    result = tmp.numberOfArithmeticSlices(A)
    print(result)
