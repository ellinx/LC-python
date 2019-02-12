"""
Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

1. push(int x), which pushes an integer x onto the stack.
2. pop(), which removes and returns the most frequent element in the stack.
3. If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.


Example 1:
Input:
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].


Note:

Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
The total number of FreqStack.push calls will not exceed 10000 in a single test case.
The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.
"""
class FreqStack:

    def __init__(self):
        self.stk = collections.deque()
        self.pq = []
        self.counter = dict()
        self.removed = dict()

    def push(self, x: 'int') -> 'None':
        self.stk.append(x)
        idx = len(self.stk)-1
        self.counter[x] = self.counter.get(x,0)+1
        # [freq, latest_idx, x]
        heapq.heappush(self.pq, [-self.counter[x], -idx, x])
        #print(self.stk, self.counter, self.pq)

    def pop(self) -> 'int':
        #print(self.stk, self.counter, self.pq)
        freq, idx, ret = heapq.heappop(self.pq)
        self.counter[ret] -= 1
        if self.counter[ret]==0:
            self.counter.pop(ret)
        if ret not in self.removed:
            self.removed[ret] = set()
        self.removed[ret].add(-idx)
        #print(self.removed)
        while len(self.stk)>0 and self.stk[-1] in self.removed and (len(self.stk)-1) in self.removed[self.stk[-1]]:
            key = self.stk.pop()
            self.removed[key].remove(len(self.stk))
            if len(self.removed[key])==0:
                self.removed.pop(key)
        return ret






# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
