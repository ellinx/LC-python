"""
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree.
It contains an integer followed by zero, one or two pairs of parenthesis.
The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   /
  3   1 5

Note:

1. There will only be '(', ')', '-' and '0' ~ '9' in the input string.
2. An empty tree is represented by "" instead of "()".

"""
class Solution:
    """
    Thoughts:
    1. parse out root, left part substring, right part substring

    Time: O()
    Space: O()
    """
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if len(s)==0:
            return None
        if "(" not in s:
            return TreeNode(int(s))
        index1 = 0
        while index1<len(s):
            if s[index1]=="(":
                break
            index1 += 1
        ret = TreeNode(int(s[:index1]))
        index2 = index1+1
        left = 0
        while index2<len(s):
            if s[index2]=="(":
                left += 1
            elif s[index2]==')':
                if left==0:
                    break
                else:
                    left -= 1
            index2 += 1
        if index2==len(s)-1:
            #print("left=",s[index1+1:index2])
            ret.left = self.str2tree(s[index1+1:index2])
        else:
            #print("left=",s[index1+1:index2],"right=",s[index2+2:-1])
            ret.left = self.str2tree(s[index1+1:index2])
            ret.right = self.str2tree(s[index2+2:-1])
        return ret
