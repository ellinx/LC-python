"""
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:

      2           1
     / \         / \
    1   4       0   3

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]

Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]

Example 5:

    1       8
     \     /
      8   1

Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]


"""

from typing import List
import TreeNode

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def getNext(node: TreeNode, first: bool, stk: List[TreeNode]) -> TreeNode:
            ret = None
            if not first:
                node = node.right
            while node is not None or len(stk) > 0:
                if node is not None:
                    stk.append(node)
                    node = node.left
                else:
                    node = stk.pop()
                    ret = node
                    break
            return ret

        ret = []
        stk1, stk2 = [], []
        node1, node2 = getNext(root1, True, stk1), getNext(root2, True, stk2)
        while node1 is not None and node2 is not None:
            if node1.val <= node2.val:
                ret.append(node1.val)
                node1 = getNext(node1, False, stk1)
            else:
                ret.append(node2.val)
                node2 = getNext(node2, False, stk2)
        while node1 is not None:
            ret.append(node1.val)
            node1 = getNext(node1, False, stk1)
        while node2 is not None:
            ret.append(node2.val)
            node2 = getNext(node2, False, stk2)
        return ret




if __name__ == "__main__":
    test = Solution()

