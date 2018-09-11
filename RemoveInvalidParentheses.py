import collections
"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:
Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:
Input: ")("
Output: [""]
"""
class Solution:
    # DFS
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            left = 0
            for c in s:
                if c=="(":
                    left += 1
                elif c==")":
                    if left==0:
                        return False
                    left -= 1
            return left==0

        def dfs(s, start, l, r, ret):
            if l==0 and r==0:
                if isValid(s):
                    ret.append(s)
                return
            if r:
                for i in range(start,len(s)):
                    if s[i]==")":
                        if i==0 or s[i-1]!=")":
                            dfs(s[:i]+s[i+1:], i, l, r-1, ret)
            if l:
                for i in range(start,len(s)):
                    if s[i]=="(":
                        if i==0 or s[i-1]!="(":
                            dfs(s[:i]+s[i+1:], i, l-1, r, ret)

        l, r = 0, 0
        for c in s:
            if c=="(":
                l += 1
            elif c==")":
                if l==0:
                    r += 1
                else:
                    l -= 1
        ret = []
        dfs(s, 0, l, r, ret)
        return ret

class Solution2:
    # BFS
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            left = 0
            for c in s:
                if c=='(':
                    left += 1
                elif c==')':
                    if left==0:
                        return False
                    left -= 1
            return left==0

        left = 0
        linvalid,rinvalid = 0,0
        for c in s:
            if c=='(':
                left += 1
            elif c==')':
                if left==0:
                    rinvalid += 1
                else:
                    left -= 1
        linvalid = left
        ret = []
        q = collections.deque()
        processed = set()
        q.append([s,linvalid,rinvalid])
        processed.add(s)
        while len(q):
            cur = q.popleft()
            if cur[1]==0 and cur[2]==0:
                if isValid(cur[0]):
                    ret.append(cur[0])
                    continue
            if cur[1]:
                for i in range(len(cur[0])):
                    if cur[0][i]=='(':
                        nxt = cur[0][:i]+cur[0][i+1:]
                        if nxt not in processed:
                            q.append([nxt,cur[1]-1,cur[2]])
                            processed.add(nxt)
            if cur[2]:
                for i in range(len(cur[0])):
                    if cur[0][i]==')':
                        nxt = cur[0][:i]+cur[0][i+1:]
                        if nxt not in processed:
                            q.append([nxt,cur[1],cur[2]-1])
                            processed.add(nxt)
        return ret
