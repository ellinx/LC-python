"""
Given a string that contains only digits 0-9 and a target value,
return all possibilities to add binary operators (not unary) +, -, or * between the digits
so they evaluate to the target value.

Example 1:
Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]

Example 2:
Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]

Example 3:
Input: num = "105", target = 5
Output: ["1*0+5","10-5"]

Example 4:
Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]

Example 5:
Input: num = "3456237490", target = 9191
Output: []
"""
class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':
        def dfs(num, start, curExp, curRes, last, target, ret):
            if start==len(num):
                if curRes==target:
                    ret.append("".join(curExp))
                return
            if num[start]=="0":
                dfs(num, start+1, curExp+["+0"], curRes, 0, target, ret)
                dfs(num, start+1, curExp+["-0"], curRes, 0, target, ret)
                dfs(num, start+1, curExp+["*0"], curRes-last, 0, target, ret)
                return
            for i in range(start+1, len(num)+1):
                nxtStr = num[start:i]
                nxt = int(nxtStr)
                dfs(num, i, curExp+["+"+nxtStr], curRes+nxt, nxt, target, ret)
                dfs(num, i, curExp+["-"+nxtStr], curRes-nxt, -nxt, target, ret)
                dfs(num, i, curExp+["*"+nxtStr], curRes-last+last*nxt, last*nxt, target, ret)


        ret = []
        if len(num)==0:
            return []
        if num[0]=="0":
            dfs(num, 1, ["0"], 0, 0, target, ret)
            return ret
        for i in range(1,len(num)+1):
            firstStr = num[:i]
            first = int(firstStr)
            dfs(num, i, [firstStr], first, first, target, ret)
        return ret
