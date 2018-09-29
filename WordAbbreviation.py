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
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.total = 0
        self.children = dict()

class Solution:
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        def addWord(root, word):
            for c in word:
                root.total += 1
                if c not in root.children:
                    root.children[c] = TrieNode()
                root = root.children[c]
            root.isWord = True

        # count how many words has same abbr
        counter = collections.defaultdict(int)
        for word in dict:
            if len(word)<=3:
                continue
            counter[word[0]+str(len(word)-2)+word[-1]] += 1
        #print(counter)

        # for each abbr which comes from more than one word, give it a trie root node
        root = {}
        for word in dict:
            if len(word)<=3:
                continue
            abbr = word[0]+str(len(word)-2)+word[-1]
            if counter[abbr]>1:
                if abbr not in root:
                    root[abbr] = TrieNode()
                addWord(root[abbr], word)
        #print(root)

        # produce result
        ret = []
        for word in dict:
            if len(word)<=3:
                ret.append(word)
                continue
            key = word[0]+str(len(word)-2)+word[-1]
            if key not in root:
                ret.append(key)
                continue
            cur, abbr = root[key], ""
            #print(word)
            for i,c in enumerate(word):
                #print(c, cur.children[c].children.keys(), cur.children[c].total)
                if cur.children[c].total==1:
                    if cur.children[c].isWord:
                        ret.append(word)
                    else:
                        abbr += c+str(len(word)-i-2)+word[-1]
                        #print(c, word, abbr)
                        if len(abbr)>=len(word):
                            ret.append(word)
                        else:
                            ret.append(abbr)
                    break
                abbr += c
                cur = cur.children[c]
        return ret
