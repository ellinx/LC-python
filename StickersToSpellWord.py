"""
We are given N different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given target string by cutting individual letters from
your collection of stickers and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the target?
If the task is impossible, return -1.

Example 1:
Input:
["with", "example", "science"], "thehat"
Output:
3

Explanation:
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.

Example 2:
Input:
["notice", "possible"], "basicbasic"
Output:
-1

Explanation:
We can't form the target "basicbasic" from cutting letters from the given stickers.

Note:

1. stickers has length in the range [1, 50].
2. stickers consists of lowercase English words (without apostrophes).
3. target has length in the range [1, 15], and consists of lowercase English letters.
4. In all test cases, all words were chosen randomly from the 1000 most common US English words,
    and the target was chosen as a concatenation of two random words.
5. The time limit may be more challenging than usual.
    It is expected that a 50 sticker test case can be solved within 35ms on average.
"""
class Solution:
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        def helper(stkCounter, target, mm):
            if target in mm:
                return mm[target]
            tarCounter = collections.Counter(target)
            ret = float('inf')
            for each in stkCounter:
                if target[0] not in each:
                    continue
                nxt = ""
                for k in tarCounter:
                    if tarCounter[k]<=each.get(k,0):
                        continue
                    nxt += k*(tarCounter[k]-each[k])
                ret = min(ret, 1+helper(stkCounter, nxt, mm))
            mm[target] = ret
            #print(mm)
            return ret

        stkCounter = []
        for sticker in stickers:
            stkCounter.append(collections.Counter(sticker))
        mm = dict()
        mm[""] = 0
        helper(stkCounter, target, mm)
        if mm[target]==float('inf'):
            return -1
        return mm[target]
