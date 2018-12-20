"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.)
According to lexicographical rules "apple" > "app",
because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Note:

1. 1 <= words.length <= 100
2. 1 <= words[i].length <= 20
3. order.length == 26
4. All characters in words[i] and order are english lowercase letters.
"""
class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        def helper(w1, w2, mm):
            i1, i2 = 0, 0
            while i1<len(w1) and i2<len(w2):
                if w1[i1]==w2[i2]:
                    i1 += 1
                    i2 += 1
                    continue
                if mm[w1[i1]]>mm[w2[i2]]:
                    return False
                return True
            if i1==len(w1) and i2<len(w2):
                return True
            return False

        mm = dict()
        for i,c in enumerate(order):
            mm[c] = i
        for i in range(1, len(words)):
            if not helper(words[i-1],words[i],mm):
                return False
        return True
