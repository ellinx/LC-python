"""
Given a char array representing tasks CPU need to do.
It contains capital letters A to Z where different letters represent different tasks.
Tasks could be done without original order.
Each task could be done in one interval.
For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks,
there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

Note:
1. The number of tasks is in the range [1, 10000].
2. The integer n is in the range [0, 100].

"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        max_freq = 0
        num_of_max_freq = 0
        for k in counter:
            if counter[k]==max_freq:
                num_of_max_freq += 1
            elif counter[k]>max_freq:
                max_freq = counter[k]
                num_of_max_freq = 1
        if num_of_max_freq>=n+1:
            return len(tasks)
        return max((n+1)*(max_freq-1)+num_of_max_freq, len(tasks))
