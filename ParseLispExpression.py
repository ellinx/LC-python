"""
You are given a string expression representing a Lisp-like expression to return the integer value of.

The syntax for these expressions is given as follows.

An expression is either an integer, a let-expression, an add-expression, a mult-expression, or an assigned variable.
Expressions always evaluate to a single integer.
(An integer could be positive or negative.)

A let-expression takes the form (let v1 e1 v2 e2 ... vn en expr), where let is always the string "let",
then there are 1 or more pairs of alternating variables and expressions, meaning that the first variable v1 is assigned
the value of the expression e1, the second variable v2 is assigned the value of the expression e2, and so on sequentially;
and then the value of this let-expression is the value of the expression expr.

An add-expression takes the form (add e1 e2) where add is always the string "add", there are always two expressions e1, e2,
and this expression evaluates to the addition of the evaluation of e1 and the evaluation of e2.

A mult-expression takes the form (mult e1 e2) where mult is always the string "mult", there are always two expressions e1, e2,
and this expression evaluates to the multiplication of the evaluation of e1 and the evaluation of e2.

For the purposes of this question, we will use a smaller subset of variable names.
A variable starts with a lowercase letter, then zero or more lowercase letters or digits.
Additionally for your convenience, the names "add", "let", or "mult" are protected and will never be used as variable names.

Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of that evaluation,
the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially.
It is guaranteed that every expression is legal. Please see the examples for more details on scope.

Evaluation Examples:

Input: (add 1 2)
Output: 3

Input: (mult 3 (add 2 3))
Output: 15

Input: (let x 2 (mult x 5))
Output: 10

Input: (let x 2 (mult x (let x 3 y 4 (add x y))))
Output: 14
Explanation: In the expression (add x y), when checking for the value of the variable x,
                we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
                Since x = 3 is found first, the value of x is 3.

Input: (let x 3 x 2 x)
Output: 2
Explanation: Assignment in let statements is processed sequentially.

Input: (let x 1 y 2 x (add x y) (add x y))
Output: 5
Explanation: The first (add x y) evaluates as 3, and is assigned to x.
                The second (add x y) evaluates as 3+2 = 5.

Input: (let x 2 (add (let x 3 (let x 4 x)) x))
Output: 6
Explanation: Even though (let x 4 x) has a deeper scope, it is outside the context of the final x in the add-expression.
                That final x will equal 2.

Input: (let a1 3 b2 (add a1 1) b2)
Output 4
Explanation: Variable names can contain digits after the first character.

Note:
1. The given string expression is well formatted: There are no leading or trailing spaces,
    there is only a single space separating different components of the string, and no space between adjacent parentheses.
    The expression is guaranteed to be legal and evaluate to an integer.
2. The length of expression is at most 2000. (It is also non-empty, as that would not be a legal expression.)
3. The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.
"""
class Solution:
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        def getNextVal(s, idx, scopes):
            if s[idx]=='(':
                left, end = 0, idx
                while end<len(s):
                    if s[end]=='(':
                        left += 1
                    elif s[end]==')':
                        left -= 1
                        if left==0:
                            break
                    end += 1
                return [calc(s[idx:end+1], scopes), end+2]
            end = idx
            while end<len(s) and s[end]!=' ':
                end += 1
            return [getVarVal(s[idx:end], scopes), end+1]

        def getNextVar(s, idx):
            end = idx
            while end<len(s) and s[end]!=" ":
                end += 1
            return [s[idx:end], end+1]


        def getVarVal(x, scopes):
            try:
                ret = int(x)
                return ret
            except:
                for mm in reversed(scopes):
                    if x in mm:
                        return mm[x]
                return 0

        def calc(s, scopes):
            #print("enter calc:", s)
            scopes.append(dict())
            s = s[1:-1]
            if s[0]=='a':
                num1, idx = getNextVal(s, len("add")+1, scopes)
                #print(num1, idx)
                num2, idx = getNextVal(s, idx, scopes)
                #print(num2, idx)
                scopes.pop()
                return num1+num2
            if s[0]=='m':
                num1, idx = getNextVal(s, len("mult")+1, scopes)
                #print(num1, idx)
                num2, idx = getNextVal(s, idx, scopes)
                #print(num2, idx)
                scopes.pop()
                return num1*num2
            if s[0]=='l':
                idx = len("let")+1
                while idx<len(s):
                    if s[idx]=='(':
                        ret = calc(s[idx:], scopes)
                        scopes.pop()
                        #print("1-", ret)
                        return ret
                    var, idx = getNextVar(s, idx)
                    if idx>=len(s):
                        ret = getVarVal(var, scopes)
                        scopes.pop()
                        #print("2-", ret)
                        return ret
                    val, idx = getNextVal(s, idx, scopes)
                    #print(var, val, idx)
                    scopes[-1][var] = val
            return None

        return calc(expression, collections.deque())
