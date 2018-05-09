"""
Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

"""


class LongestRepeatingCharacterReplacement:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        letters = [0]*26
        start, end = 0, 0
        maxSameCharCount = 0
        res = 0

        for end in range(len(s)):
            letters[ord(s[end])-ord('A')] += 1
            maxSameCharCount = max(maxSameCharCount, letters[ord(s[end])-ord('A')])

            while end-start+1-maxSameCharCount > k:
                letters[ord(s[start])-ord('A')] -= 1
                start += 1

                maxSameCharCount = 0
                for count in letters:
                    maxSameCharCount = max(maxSameCharCount, count)

            res = max(res, end-start+1)

        return res


# test
if __name__=="__main__":
    tmp = LongestRepeatingCharacterReplacement()
    result = tmp.characterReplacement("AABABBA",1)
    print(result)