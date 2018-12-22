"""
Write a function to generate the generalized abbreviations of a word.

Note: The order of the output does not matter.

Example:

Input: "word"
Output:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", 
"1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""
class Solution:
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def helper(word, start, cur, count, ret):
            if start>=len(word):
                if count>0:
                    cur += str(count)
                ret.append(cur)
                return
            if count>0:
                helper(word, start+1, cur+str(count)+word[start], 0, ret)
            else:
                helper(word, start+1, cur+word[start], 0, ret)
            helper(word, start+1, cur, count+1, ret)


        ret = []
        helper(word, 0, "", 0, ret)
        return ret
