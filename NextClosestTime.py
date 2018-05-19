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

class NextClosestTime:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        def isValidTime(time):
            return int(time[:2])<24 and int(time[2:])<60

        def dist(val, time):
            temp = int(time[:2])*60+int(time[2:])-val
            if temp>0:
                return temp
            return temp+23*60+59

        ret = None
        base = set(time[:2]+time[3:])
        baseVal = int(time[:2])*60+int(time[3:])
        li = [ c for c in base ]
        for i in range(3):
            nxt = []
            for each in li:
                for c in base:
                    nxt.append(each+c)
            li = nxt
        #print(li)
        li = filter(isValidTime, li)
        for each in li:
            if not ret:
                ret = (each, dist(baseVal, each))
                continue
            distVal = dist(baseVal, each)
            if ret[1]>distVal:
                ret = (each, distVal)
            #print(ret)
        return ret[0][:2]+':'+ret[0][2:]
