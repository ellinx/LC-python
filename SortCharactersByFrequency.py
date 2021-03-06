import collections
"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""


class SortCharactersByFrequency:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        ret = ''
        for k,num in counter.most_common():
            ret += k*num
        return ret


# test
if __name__=="__main__":
    tmp = SortCharactersByFrequency()
    result = tmp.frequencySort("Aabb")
    print(result)
