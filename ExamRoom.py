"""
In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.
If there are multiple such seats, they sit in the seat with the lowest number.
(Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions:
ExamRoom.seat() returning an int representing what seat the student sat in,
and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.

It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.


Example 1:

Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]

Explanation:
ExamRoom(10) -> null
seat() -> 0, no one is in the room, then the student sits at seat number 0.
seat() -> 9, the student sits at the last seat number 9.
seat() -> 4, the student sits at the last seat number 4.
seat() -> 2, the student sits at the last seat number 2.
leave(4) -> null
seat() -> 5, the student​​​​​​​ sits at the last seat number 5.
​​​​​​​

Note:

1. 1 <= N <= 10^9
2. ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
3. Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.
"""
class ExamRoom:

    def __init__(self, N):
        """
        :type N: int
        """
        self.N = N
        self.seats = []

    def seat(self):
        """
        :rtype: int
        """
        if len(self.seats)==0:
            self.seats.append(0)
            return 0
        # [pos, insertIndex, dist]
        cur = [-1, -1, 0]
        for i in range(1,len(self.seats)):
            dist = (self.seats[i]-self.seats[i-1])//2
            if dist>cur[2]:
                cur = [self.seats[i-1]+dist, i, dist]
        if self.seats[0]!=0 and self.seats[0]>=cur[2]:
            cur = [0, 0, self.seats[0]]
        if self.seats[-1]!=self.N-1 and self.N-1-self.seats[-1]>cur[2]:
            cur = [self.N-1, len(self.seats), self.N-1-self.seats[-1]]
        self.seats.insert(cur[1], cur[0])
        #print("sit ", self.seats)
        return cur[0]

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        l, r = 0, len(self.seats)-1
        while l<=r:
            m = l+(r-l)//2
            if self.seats[m]==p:
                self.seats.pop(m)
                #print("leave ",self.seats)
                return
            if self.seats[m]<p:
                l = m+1
            else:
                r = m-1


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
