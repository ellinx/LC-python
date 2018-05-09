class MinimumMovesToEqualArrayElements:
    """
    Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements
    equal, where a move is incrementing n - 1 elements by 1.

    Example:

    Input:
    [1,2,3]

    Output:
    3

    Explanation:
    Only three moves are needed (remember each move increments two elements):

    [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
    """
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # incrementing n - 1 elements by 1 <=> decrease 1 element by 1
        res = 0
        minNum = min(nums)
        for num in nums:
            res += num - minNum

        return res

    """
    Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where 
    a move is incrementing a selected element by 1 or decrementing a selected element by 1.

    You may assume the array's length is at most 10,000.

    Example:
    
    Input:
    [1,2,3]
    
    Output:
    2
    
    Explanation:
    Only two moves are needed (remember each move increments or decrements one element):
    
    [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
    """
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        left = 0
        right = len(nums)-1
        while left<right:
            res += nums[right] - nums[left]
            left += 1
            right -= 1

        return res


# test
if __name__=="__main__":
    tmp = MinimumMovesToEqualArrayElements()
    nums = [1,2,3]
    result = tmp.minMoves2(nums)
    print(result)