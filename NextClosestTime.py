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
        def dfsAndCheck(nums, cur, ori, closest):
            if len(cur)==4:
                dist = int(cur[:2])*60+int(cur[2:])-ori
                if dist==0:
                    return
                if dist<0:
                    dist += 24*60
                if dist<closest[0]:
                    closest[0] = dist
                    closest[1] = cur[:2]+":"+cur[2:]
                return
            for i in range(len(nums)):
                nxt = cur+nums[i]
                if (len(nxt)>=2 and int(nxt[:2])>=24) or (len(nxt)==4 and int(nxt[2:])>=60):
                    continue
                dfsAndCheck(nums, nxt, ori, closest)


        digits = ""
        for c in time:
            if c.isdigit() and c not in digits:
                digits += c
        ret = [float('inf'), ""]
        dfsAndCheck(digits, "", int(time[:2])*60+int(time[3:]), ret)
        if ret[1]=="":
            return time
        return ret[1]
