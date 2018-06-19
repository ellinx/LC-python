"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:
Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.

Example 2:
Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
"""

class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        def dfs(nums, cur, allTimes):
            if len(cur)==4:
                if int(cur[-2:])<60:
                    allTimes.append(cur)
                return
            if len(cur)==2 and int(cur)>23:
                return
            for i in range(len(nums)):
                dfs(nums, cur+nums[i], allTimes)

        nums = []
        for c in time:
            if c.isdigit() and c not in nums:
                nums.append(c)
        allTimes = []
        dfs(nums, "", allTimes)
        #print(allTimes)
        minDiff = 24*60
        ret = None
        cur = int(time[:2])*60+int(time[3:])
        for each in allTimes:
            if each==time[:2]+time[3:]:
                continue
            diff = int(each[:2])*60+int(each[2:])-cur
            if diff<0:
                diff = 24*60+diff
            if minDiff>diff:
                minDiff = diff
                ret = each
        return ret[:2]+":"+ret[2:] if ret else time
