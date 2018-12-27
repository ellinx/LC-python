import heapq
"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = []
        for i in range(len(nums)):
            heapq.heappush(pq, nums[i])
            if len(pq)>k:
                heapq.heappop(pq)
        return pq[0]


class Solution2:
    # similar to quick sort
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def helper(nums, start, end, k):
            #print(nums, start, end, k)
            pivot = nums[start]
            l, r = start+1, end
            while l<=r:
                while l<=end and nums[l]>=pivot:
                    l += 1
                while r>start and nums[r]<pivot:
                    r -= 1
                if l>r:
                    break
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            #print(l,r)
            rank = l-start
            if rank==k:
                return pivot
            nums[r], nums[start] = nums[start], nums[r]
            if rank<k:
                return helper(nums, l, end, k-rank)
            else:
                return helper(nums, start, r-1, k)

        return helper(nums, 0, len(nums)-1, k)

if __name__=='__main__':
    temp = KthLargestElementInAnArray()
    nums = [3,2,1,5,6,4]
    k = 2
    result = temp.findKthLargest(nums,k)
    print(result)
