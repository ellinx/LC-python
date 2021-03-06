"""
Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word".
Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:
Given s = "internationalization", abbr = "i12iz4n":

Return true.
Example 2:
Given s = "apple", abbr = "a2e":

Return false.
"""
class Solution:
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        idx = 0
        l, r = 0, 0
        while l<len(abbr):
            if abbr[r].isalpha():
                #print(r, idx, abbr[r], word[idx])
                if idx>=len(word) or abbr[r]!=word[idx]:
                    return False
                r += 1
                l = r
                idx += 1
                continue
            while r<len(abbr) and abbr[r].isdigit():
                r += 1
            # have leading zero or zero
            if abbr[l]=='0':
                return False
            idx += int(abbr[l:r])
            l = r
        return idx==len(word)
