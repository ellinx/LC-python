"""
In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function:
TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.

Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.


Example 1:
Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation:
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.


Note:
1. 1 <= persons.length = times.length <= 5000
2. 0 <= persons[i] <= persons.length
3. times is a strictly increasing array with all elements in [0, 10^9].
4. TopVotedCandidate.q is called at most 10000 times per test case.
5. TopVotedCandidate.q(int t) is always called with t >= times[0].
"""
class TopVotedCandidate:

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        mm = dict()
        self.timeline = []
        # [number of votes, last vote time, person]
        top = [0, -1, -1]
        for i in range(len(persons)):
            tmp = mm.get(persons[i], [0, -1])
            tmp[0] += 1
            tmp[1] = times[i]
            mm[persons[i]] = tmp
            if tmp[0]>top[0] or (tmp[0]==top[0] and tmp[1]>top[1]):
                top = [tmp[0], tmp[1], persons[i]]
            self.timeline.append([top[1], top[2]])

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        s, e = 0, len(self.timeline)-1
        while s<=e:
            m = s+(e-s)//2
            if self.timeline[m][0]==t:
                return self.timeline[m][1]
            if self.timeline[m][0]<t:
                s = m+1
            else:
                e = m-1
        return self.timeline[s-1][1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)


class TopVotedCandidate2:

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.votes = collections.defaultdict(list)
        for i in range(len(persons)):
            self.votes[persons[i]].append(times[i])

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        pq = []
        for p in self.votes:
            idx = bisect.bisect_right(self.votes[p], t)
            if idx>0:
                heapq.heappush(pq, [-idx, -self.votes[p][idx-1], p])
        return heapq.heappop(pq)[2]
