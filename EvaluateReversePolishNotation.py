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
        for each in tokens:
            if each in "+-*/":
                num2 = stk.pop()
                num1 = stk.pop()
                if each=="+":
                    stk.append(num1+num2)
                elif each=="-":
                    stk.append(num1-num2)
                elif each=="*":
                    stk.append(num1*num2)
                else:
                    result = num1/num2
                    if result>=0:
                        result = math.floor(result)
                    else:
                        result = math.ceil(result)
                    stk.append(result)
            else:
                stk.append(int(each))
            #print(stk)
        #print(stk)
        return stk[0]


# test
if __name__ == "__main__":
    tmp = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    result = tmp.evalRPN(tokens)
    print(result)
