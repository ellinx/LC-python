"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters
and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:
1. A word is defined as a character sequence consisting of non-space characters only.
2. Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
3. The input array words contains at least one word.

Example 1:
Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.

Example 3:
Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""
class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def getLine(words, l, r, total, maxWidth):
            totalSpace = maxWidth-total
            if l==r:
                return words[l]+" "*totalSpace
            baseSpace = totalSpace//(r-l)
            remainSpace = totalSpace%(r-l)
            ret = ""
            for i in range(l,r):
                ret += words[i]+" "*baseSpace
                if remainSpace:
                    ret += " "
                    remainSpace -= 1
            ret += words[r]
            return ret

        ret = []
        l, r = 0, 0
        while l<len(words):
            total = 0
            while r<len(words):
                total += len(words[r])
                if total+r-l>=maxWidth:
                    break
                r += 1
            if r==len(words):
                r -= 1
            if total+r-l<maxWidth:
                missing = maxWidth-(total+r-l)
                tmp = ""
                for i in range(l,r+1):
                    tmp += words[i]
                    if i!=r:
                        tmp += " "
                tmp += " "*missing
                ret.append(tmp)
                break
            if total+r-l>maxWidth:
                total -= len(words[r])
                r -= 1
            ret.append(getLine(words, l, r, total, maxWidth))
            l, r = r+1, r+1
        return ret
