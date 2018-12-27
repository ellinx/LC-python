import collections
"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = collections.deque()
        for token in tokens:
            if token in "+-*/":
                op2 = stk.pop()
                op1 = stk.pop()
                if token=='+':
                    stk.append(op1+op2)
                elif token=='-':
                    stk.append(op1-op2)
                elif token=='*':
                    stk.append(op1*op2)
                elif token=='/':
                    stk.append(int(op1/op2))
                continue
            stk.append(int(token))
        return stk[0]


# test
if __name__ == "__main__":
    tmp = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    result = tmp.evalRPN(tokens)
    print(result)
