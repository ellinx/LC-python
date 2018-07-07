"""
An abbreviation of a word follows the form <first letter><number><last letter>.
Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
     ↓
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
     ↓   ↓    ↓    ↓  ↓
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
     ↓   ↓    ↓
d) l|ocalizatio|n          --> l10n

Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary.
A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:

Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true


"""
class ValidWordAbbr:

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        counter = collections.defaultdict(set)
        for word in dictionary:
            if len(word)<3:
                counter[word].add(word)
                continue
            k = word[0]+str(len(word)-2)+word[-1]
            counter[k].add(word)
        self.abbrs = counter
        #print(self.abbrs)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)<3:
            k = word
        else:
            k = word[0]+str(len(word)-2)+word[-1]
        if k not in self.abbrs:
            return True
        if len(self.abbrs[k])==1 and word in self.abbrs[k]:
            return True
        return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
