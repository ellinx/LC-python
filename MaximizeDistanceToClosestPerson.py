"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Example 2:

Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

Note:

1. 1 <= seats.length <= 20000
2. seats contains only 0s or 1s, at least one 0, and at least one 1.


"""
class Solution:
    """
    Thoughts:
    1. record seats that has person sit.
    2. loop through and check for longest possible distance

    Time: O(n) where n is length of seats
    Space: O(n)
    """
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        people = []
        for i in range(len(seats)):
            if seats[i]==1:
                people.append(i)
        ret = 0
        for i in range(1,len(people)):
            ret = max(ret,(people[i]-people[i-1])//2)
        # check head and tail
        if people[0]!=0:
            ret = max(ret, people[0])
        if people[-1]!=len(seats)-1:
            ret = max(ret, len(seats)-1-people[-1])
        return ret
