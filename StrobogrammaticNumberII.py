"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
"""
class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def firstHalfList(numMap, size):
            part1List = [k for k in numMap if k!="0"]
            for i in range(size-1):
                nextList = []
                for j in range(len(part1List)):
                    for k in numMap:
                        nextList.append(part1List[j] + k)
                part1List = nextList
            return part1List

        numMap = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        ret = []
        if n==1:
            return ["0","1","8"]
        if n%2==0:
            part1List = firstHalfList(numMap, n//2)
            for i in range(len(part1List)):
                part2 = ""
                for c in part1List[i][::-1]:
                    part2 += numMap[c]
                part1List[i] += part2
        else:
            part1List = firstHalfList(numMap, (n-1)//2)
            nextList = []
            for i in range(len(part1List)):
                for mid in "018":
                    part2 = ""
                    for c in part1List[i][::-1]:
                        part2 += numMap[c]
                    nextList.append(part1List[i]+mid+part2)
            part1List = nextList
        return part1List
