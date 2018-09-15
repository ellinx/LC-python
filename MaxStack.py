"""
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.

Example 1:
MaxStack stack = new MaxStack();
stack.push(5);
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5

Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
"""
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.vals = collections.deque()
        self.max = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.vals.append(x)
        if len(self.max)==0 or self.max[-1]<=x:
            self.max.append(x)

    def pop(self):
        """
        :rtype: int
        """
        ret = self.vals.pop()
        if ret == self.max[-1]:
            self.max.pop()
        return ret

    def top(self):
        """
        :rtype: int
        """
        return self.vals[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.max[-1]

    def popMax(self):
        """
        :rtype: int
        """
        ret = self.max.pop()
        tmp = collections.deque()
        while self.vals[-1]!=ret:
            tmp.append(self.vals.pop())
        self.vals.pop()
        while len(tmp):
            x = tmp.pop()
            self.vals.append(x)
            if len(self.max)==0 or self.max[-1]<=x:
                self.max.append(x)
        return ret


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
