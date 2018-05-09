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
        map = dict()
        res = ""
        for i in range(len(s)):

            if s[i] in map:
                map[s[i]] += 1
            else:
                map[s[i]] = 1

        maxHeap = sorted(list(map.items()),key=lambda x: -x[1])

        for each in maxHeap:
            res += each[0]*each[1]

        return res


# test
if __name__=="__main__":
    tmp = SortCharactersByFrequency()
    result = tmp.frequencySort("Aabb")
    print(result)