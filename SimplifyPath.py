"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""
class Solution:
    """
    Thoughts:
    1. use stack

    Time: O(n) where n is length of path
    Space: O(n)
    """
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not len(path):
            return ""
        names = path.split("/")
        stk = collections.deque()
        for each in names:
            if each=="" or each==".":
                continue
            if each=="..":
                if len(stk):
                    stk.pop()
            else:
                stk.append(each)
        return "/"+"/".join(stk)
