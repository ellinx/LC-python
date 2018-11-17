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
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def dfs(num, start, cur, val, last, target, ret):
            if start==len(num):
                if val==target:
                    ret.append(cur)
                return
            for i in range(start,len(num)):
                if num[start]=='0':
                    dfs(num, start+1, cur+"+0", val, 0, target, ret)
                    dfs(num, start+1, cur+"-0", val, 0, target, ret)
                    dfs(num, start+1, cur+"*0", val-last, 0, target, ret)
                    break
                d = num[start:i+1]
                # +
                dfs(num, i+1, cur+"+"+d, val+int(d), int(d), target, ret)
                # -
                dfs(num, i+1, cur+"-"+d, val-int(d), -int(d), target, ret)
                # *
                dfs(num, i+1, cur+"*"+d, val-last+last*int(d), last*int(d), target, ret)

        ret = []
        if len(num)==0:
            return ret
        for i in range(len(num)):
            if num[0]=='0':
                dfs(num, 1, "0", 0, 0, target, ret)
                break
            dfs(num, i+1, num[:i+1], int(num[:i+1]), int(num[:i+1]), target, ret)
        return ret
