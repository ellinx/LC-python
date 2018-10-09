"""
Implement a MyCalendar class to store your events.
A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end).
Formally, this represents a booking on the half open interval [start, end),
the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection
(ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be
added to the calendar successfully without causing a double booking.
Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
Note:

1. The number of calls to MyCalendar.book per test case will be at most 1000.
2. In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
"""
class MyCalendar:

    def __init__(self):
        self.q = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        def insertIndex(events, start):
            s, e = 0, len(events)-1
            while s<=e:
                m = s+(e-s)//2
                if events[m][0]==start:
                    return m
                if events[m][0]<start:
                    s = m+1
                else:
                    e = m-1
            return s

        idx = insertIndex(self.q, start)
        if idx==len(self.q):
            if len(self.q)==0 or start>=self.q[-1][1]:
                self.q.append([start,end])
                return True
            return False
        if self.q[idx][0]<end:
            return False
        if idx-1>=0 and self.q[idx-1][1]>start:
            return False
        self.q.insert(idx, [start,end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
