"""
You are given several logs that each log contains a unique id and timestamp.
Timestamp is a string that has the following format: Year:Month:Day:Hour:Minute:Second,
for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.

Design a log storage system to implement the following functions:

void Put(int id, string timestamp): Given a log's unique id and timestamp, store the log in your storage system.


int[] Retrieve(String start, String end, String granularity):
Return the id of logs whose timestamps are within the range from start to end.
Start and end all have the same format as timestamp. However, granularity means the time level for consideration.
For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", granularity = "Day",
it means that we need to find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.

Example 1:
put(1, "2017:01:01:23:59:59");
put(2, "2017:01:01:22:59:59");
put(3, "2016:01:01:00:00:00");
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year");
// return [1,2,3], because you need to return all logs within 2016 and 2017.
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour");
// return [1,2], because you need to return all logs start from 2016:01:01:01 to 2017:01:01:23,
//  where log 3 is left outside the range.

Note:
1. There will be at most 300 operations of Put or Retrieve.
2. Year ranges from [2000,2017]. Hour ranges from [00,23].
3. Output for Retrieve has no order required.
"""
class LogSystem:

    def __init__(self):
        self.logs = []

    def timecomp(self, t1, t2, endIdx):
        for idx in range(endIdx+1):
            if t1[idx]==t2[idx]:
                continue
            return t1[idx]-t2[idx]
        return 0

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        time = list(map(int, timestamp.split(":")))
        l, r = 0, len(self.logs)-1
        while l<=r:
            m = l+(r-l)//2
            if self.timecomp(self.logs[m][1], time, len(time)-1)<0:
                l = m+1
            else:
                r = m-1
        self.logs.insert(l, [id, time])

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        #print(self.logs)
        unit = ["Year","Month","Day","Hour","Minute","Second"]
        endIdx = 0
        while endIdx<len(unit):
            if gra!=unit[endIdx]:
                endIdx += 1
                continue
            break
        stime = list(map(int,s.split(":")))
        l, r = 0, len(self.logs)-1
        while l<=r:
            m = l+(r-l)//2
            if self.timecomp(self.logs[m][1], stime, endIdx)==0:
                if m-1>=l and self.timecomp(self.logs[m-1][1], stime, endIdx)==0:
                    r = m-1
                    continue
                l = m
                break
            if self.timecomp(self.logs[m][1], stime, endIdx)<0:
                l = m+1
            else:
                r = m-1
        lbound = l
        if l==len(self.logs):
            return []
        etime = list(map(int,e.split(":")))
        l, r = 0, len(self.logs)-1
        while l<=r:
            m = l+(r-l)//2
            if self.timecomp(self.logs[m][1], etime, endIdx)==0:
                if m+1<=r and self.timecomp(self.logs[m+1][1], etime, endIdx)==0:
                    l = m+1
                    continue
                l = m
                break
            if self.timecomp(self.logs[m][1], etime, endIdx)<0:
                l = m+1
            else:
                r = m-1
        if l==len(self.logs):
            rbound = l
        else:
            rbound = l+1 if self.timecomp(self.logs[l][1], etime, endIdx)==0 else l
        #print(lbound, rbound)
        return [self.logs[i][0] for i in range(lbound, rbound)]



# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
