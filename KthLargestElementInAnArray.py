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
class KthLargestElementInAnArray(object):
    # heap
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap,num)
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        return minHeap[0]

    # quick sort
    def findKthLargest2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # similar to quick sort
        index = 1
        left, right = 1, len(nums)-1
        while left<=right:
            if nums[index]<=nums[0]:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
            else:
                if index==left:
                    index += 1
                    left += 1
                else:
                    nums[index], nums[left] = nums[left], nums[index]
                    left += 1
        #print(nums, left,right,k)
        if left==k:
            return nums[0]
        if left<k:
            return self.findKthLargest(nums[left:],k-left)
        else:
            return self.findKthLargest(nums[1:left],k)

if __name__=='__main__':
    temp = KthLargestElementInAnArray()
    nums = [3,2,1,5,6,4]
    k = 2
    result = temp.findKthLargest(nums,k)
    print(result)
