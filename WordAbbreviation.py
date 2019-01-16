"""
Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.

1. Begin with the first character and then the number of characters abbreviated, which followed by the last character.
2. If there are any conflict, that is more than one words share the same abbreviation,
    a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique.
    In other words, a final abbreviation cannot map to more than one original words.
3. If the abbreviation doesn't make the word shorter, then keep it as original.

Example:
Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]

Note:
1. Both n and the length of each word will not exceed 400.
2. The length of each word is greater than 1.
3. The words consist of lowercase English letters only.
4. The return answers should be in the same order as the original array.
"""
class Solution:
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        def getAbbr(word, prefix):
            if len(word)-prefix-1<2:
                return word
            return word[:prefix]+str(len(word)-prefix-1)+word[-1]

        n = len(dict)
        ret = []
        prefix = [1]*n
        for word in dict:
            if len(word)<=3:
                ret.append(word)
                continue
            ret.append(getAbbr(word, 1))
        for i in range(n):
            while True:
                dup = []
                for j in range(i+1,n):
                    if ret[i]==ret[j]:
                        dup.append(j)
                if len(dup)==0:
                    break
                dup.append(i)
                for idx in dup:
                    prefix[idx] += 1
                    ret[idx] = getAbbr(dict[idx], prefix[idx])
        return ret
