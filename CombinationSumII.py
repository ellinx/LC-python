"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:
1. All numbers (including target) will be positive integers.
2. The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
class Solution:
    def combinationSum2(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        def dfs(candidates, start, curComb, curSum, target, ret):
            #print(curComb, curSum, target)
            if curSum==target:
                ret.append(curComb)
                return
            for i in range(start, len(candidates)):
                if curSum+candidates[i]>target:
                    break
                if i>start and candidates[i-1]==candidates[i]:
                    continue
                dfs(candidates, i+1, curComb+[candidates[i]], curSum+candidates[i], target, ret)

        candidates.sort()
        ret = []
        dfs(candidates, 0, [], 0, target, ret)
        return ret
