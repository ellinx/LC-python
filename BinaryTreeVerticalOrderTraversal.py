"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]

Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]

Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]


"""
class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        dic = collections.defaultdict(list)
        q = collections.deque()
        q.append((root,0))
        while len(q):
            cur = q.popleft()
            dic[cur[1]].append(cur[0].val)
            if cur[0].left:
                q.append((cur[0].left, cur[1]-1))
            if cur[0].right:
                q.append((cur[0].right, cur[1]+1))
        leftmost, rightmost = min(dic.keys()), max(dic.keys())
        ret = [0]*(rightmost-leftmost+1)
        for k in dic:
            ret[k-leftmost] = dic[k]
        return ret
