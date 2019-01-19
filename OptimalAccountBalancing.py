"""
A group of friends went on holiday and sometimes lent each other money.
For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride.
We can model each transaction as a tuple (x, y, z) which means person x gave person y $z.
Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID),
the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

Given a list of transactions between a group of people,
return the minimum number of transactions required to settle the debt.

Note:

A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2
or we could also have the persons 0, 2, 6.

Example 1:
Input:
[[0,1,10], [2,0,5]]
Output:
2

Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.

Two transactions are needed.
One way to settle the debt is person #1 pays person #0 and #2 $5 each.

Example 2:
Input:
[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
Output:
1

Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.

Therefore, person #1 only need to give person #0 $4, and all debt is settled.
"""
class Solution:
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        def dfs(nums):
            if len(nums)==2:
                return 1
            ret = float('inf')
            for i in range(1,len(nums)):
                if nums[0]*nums[i]<0:
                    nxt = nums[1:i]+nums[i+1:]
                    if nums[0]+nums[i]!=0:
                        nxt.append(nums[0]+nums[i])
                    ret = min(ret, 1+dfs(nxt))
            return ret

        balance = dict()
        for x,y,z in transactions:
            balance[x] = balance.get(x,0)-z
            balance[y] = balance.get(y,0)+z
        nums = [balance[k] for k in balance if balance[k]!=0]
        #print(nums)
        if len(nums)==0:
            return 0
        return dfs(nums)
