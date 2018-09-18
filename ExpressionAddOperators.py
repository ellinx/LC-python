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
        def dfs(num, start, last, cur, target, ret):
            if start==len(num):
                #print(start, cur, target)
                if cur[1]==target:
                    ret.append(cur[0])
                return
            if num[start]=='0':
                # +
                dfs(num, start+1, 0, [cur[0]+"+0", cur[1]], target, ret)
                # -
                dfs(num, start+1, 0, [cur[0]+"-0", cur[1]], target, ret)
                # *
                dfs(num, start+1, 0, [cur[0]+"*0", cur[1]-last], target, ret)
                return
            for end in range(start+1,len(num)+1):
                tmp = int(num[start:end])
                # +
                dfs(num, end, tmp, [cur[0]+"+"+str(tmp), cur[1]+tmp], target, ret)
                # -
                dfs(num, end, -tmp, [cur[0]+"-"+str(tmp), cur[1]-tmp], target, ret)
                # *
                dfs(num, end, last*tmp, [cur[0]+"*"+str(tmp), cur[1]-last+last*tmp], target, ret)

        ret = []
        if len(num)==0:
            return ret
        if num[0]=='0':
            dfs(num, 1, 0, ["0", 0], target, ret)
        else:
            for i in range(1,len(num)+1):
                tmp = int(num[0:i])
                dfs(num, i, tmp, [str(tmp), tmp], target, ret)
        return ret
