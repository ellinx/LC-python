"""
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"
"""


class ReconstructOriginalDigitsFromEnglish(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = ""
        letters = [0]*26

        for each in s:
            letters[ord(each)-ord('a')] += 1

        # z,w,u,x,g identify unique digits
        if letters[ord('z')-ord('a')]>0:
            times = letters[ord('z') - ord('a')]
            res += "0"*times
            letters[ord('z')-ord('a')] -= times
            letters[ord('e')-ord('a')] -= times
            letters[ord('r')-ord('a')] -= times
            letters[ord('o')-ord('a')] -= times

        if letters[ord('w')-ord('a')]>0:
            times = letters[ord('w') - ord('a')]
            res += "2"*times
            letters[ord('t')-ord('a')] -= times
            letters[ord('w')-ord('a')] -= times
            letters[ord('o')-ord('a')] -= times

        if letters[ord('u')-ord('a')]>0:
            times = letters[ord('u') - ord('a')]
            res += "4"*times
            letters[ord('f')-ord('a')] -= times
            letters[ord('o')-ord('a')] -= times
            letters[ord('u')-ord('a')] -= times
            letters[ord('r')-ord('a')] -= times

        if letters[ord('x')-ord('a')]>0:
            times = letters[ord('x') - ord('a')]
            res += "6"*times
            letters[ord('s')-ord('a')] -= times
            letters[ord('i')-ord('a')] -= times
            letters[ord('x')-ord('a')] -= times

        if letters[ord('g')-ord('a')]>0:
            times = letters[ord('g') - ord('a')]
            res += "8"*times
            letters[ord('e')-ord('a')] -= times
            letters[ord('i')-ord('a')] -= times
            letters[ord('g')-ord('a')] -= times
            letters[ord('h')-ord('a')] -= times
            letters[ord('t')-ord('a')] -= times

        # now o,h,s identify unique digits
        if letters[ord('o')-ord('a')]>0:
            times = letters[ord('o') - ord('a')]
            res += "1"*times
            letters[ord('o')-ord('a')] -= times
            letters[ord('n')-ord('a')] -= times
            letters[ord('e')-ord('a')] -= times

        if letters[ord('h')-ord('a')]>0:
            times = letters[ord('h') - ord('a')]
            res += "3"*times
            letters[ord('t')-ord('a')] -= times
            letters[ord('h')-ord('a')] -= times
            letters[ord('r')-ord('a')] -= times
            letters[ord('e')-ord('a')] -= times
            letters[ord('e')-ord('a')] -= times

        if letters[ord('s')-ord('a')]>0:
            times = letters[ord('s') - ord('a')]
            res += "7"*times
            letters[ord('s')-ord('a')] -= times
            letters[ord('e')-ord('a')] -= times
            letters[ord('v')-ord('a')] -= times
            letters[ord('e')-ord('a')] -= times
            letters[ord('n')-ord('a')] -= times

        # f and n differentiate what's left
        if letters[ord('f')-ord('a')]>0:
            times = letters[ord('f') - ord('a')]
            res += "5"*times
            letters[ord('f')-ord('a')] -= times
            letters[ord('i')-ord('a')] -= times
            letters[ord('v')-ord('a')] -= times
            letters[ord('e')-ord('a')] -= times

        if letters[ord('n')-ord('a')]>0:
            times = letters[ord('n') - ord('a')]
            times >>= 1 # nine has two 'n'
            res += "9"*times
            letters[ord('n')-ord('a')] -= times
            letters[ord('i')-ord('a')] -= times
            letters[ord('n')-ord('a')] -= times
            letters[ord('e')-ord('a')] -= times

        return "".join(sorted(res))


# test
if __name__=="__main__":
    tmp = ReconstructOriginalDigitsFromEnglish()
    result = tmp.originalDigits("nnie")
    print(result)
