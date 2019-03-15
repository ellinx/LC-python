"""
Print a binary tree in an m*n 2D string array following these rules:

1. The row number m should be equal to the height of the given binary tree.
2. The column number n should always be an odd number.
3. The root node's value (in string format) should be put in the exactly middle of the first row it can be put.
    The column and the row where the root node belongs will separate the rest space into two parts
    (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and
    print the right subtree in the right-bottom part.
    The left-bottom part and the right-bottom part should have the same size.
    Even if one subtree is none while the other is not, you don't need to print anything for the none subtree
    but still need to leave the space as large as that for the other subtree.
    However, if two subtrees are none, then you don't need to leave space for both of them.
4. Each unused space should contain an empty string "".
5. Print the subtrees following the same rules.

Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]

Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]

Example 3:
Input:
      1
     / \
    2   5
   /
  3
 /
4
Output:
[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
"""
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def depth(root):
            if root is None:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            return max(left,right)+1

        def fill(root, i, l, r, ret):
            if root is None:
                return
            m = l+(r-l)//2
            ret[i][m] = str(root.val)
            fill(root.left, i+1, l, m-1, ret)
            fill(root.right, i+1, m+1, r, ret)

        m = depth(root)
        n = 1
        for i in range(2,m+1):
            n = 2*n+1
        ret = [[""]*n for _ in range(m)]
        fill(root, 0, 0, n-1, ret)
        return ret
