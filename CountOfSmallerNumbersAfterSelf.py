"""
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.


"""
class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def insertIndex(nums, target):
            start, end = 0, len(nums)-1
            while start<=end:
                mid = start+(end-start)//2
                if nums[mid]==target:
                    if mid==0 or nums[mid-1]!=target:
                        return mid
                    end = mid-1
                elif nums[mid]<target:
                    start = mid+1
                else:
                    end = mid-1
            return start

        ret = []
        if len(nums)==0:
            return ret
        li = sorted(nums[1:])
        for i in range(0,len(nums)-1):
            #print(li, nums[i])
            index = insertIndex(li, nums[i])
            ret.append(index)
            li.remove(nums[i+1])
        ret.append(0)
        return ret

class Solution2:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def mergeSort(nums, counts):
            if len(nums)==1:
                return nums
            mid = (len(nums)-1)//2
            l = mergeSort(nums[:mid+1], counts)
            r = mergeSort(nums[mid+1:], counts)
            ret = [0]*len(nums)
            i1, i2 = 0, 0
            while i1<len(l) and i2<len(r):
                if l[i1][0]<=r[i2][0]:
                    ret[i1+i2] = l[i1]
                    counts[l[i1][1]] += i2
                    i1 += 1
                else:
                    ret[i1+i2] = r[i2]
                    i2 += 1
            while i1<len(l):
                ret[i1+i2] = l[i1]
                counts[l[i1][1]] += i2
                i1 += 1
            while i2<len(r):
                ret[i1+i2] = r[i2]
                i2 += 1
            return ret

        counts  = [0]*len(nums)
        if len(nums)<2:
            return counts
        arr = [[nums[i],i] for i in range(len(nums))]
        mergeSort(arr, counts)
        return counts
