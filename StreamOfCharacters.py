"""
Implement the StreamChecker class as follows:

    StreamChecker(words): Constructor, init the data structure with the given words.
    query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.



Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist



Note:

    1 <= words.length <= 2000
    1 <= words[i].length <= 2000
    Words will only consist of lowercase English letters.
    Queries will only consist of lowercase English letters.
    The number of queries is at most 40000.



"""

from typing import List
import collections

class Trie:
    def __init__(self):
        self.isWord = False
        self.children = dict()

class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = Trie()
        self.s = ""
        self.maxLen = 0
        for word in words:
            cur = self.root
            self.maxLen = max(self.maxLen, len(word))
            for c in reversed(word):
                if c not in cur.children:
                    cur.children[c] = Trie()
                cur = cur.children[c]
            cur.isWord = True
            

    def query(self, letter: str) -> bool:
        self.s = letter + self.s
        node = self.root
        for c in self.s[:self.maxLen]:
            if c not in node.children:
                return False
            node = node.children[c]
            if node.isWord:
                return True
        return node.isWord
    

        
if __name__ == "__main__":
    words = ["cd","f","kl"]
    streamChecker = StreamChecker(words)
    print(streamChecker.query("a"))
    print(streamChecker.query("b"))
    print(streamChecker.query("c"))
    print(streamChecker.query("d"))
    print(streamChecker.query("e"))
    print(streamChecker.query("f"))
    print(streamChecker.query("g"))
    print(streamChecker.query("h"))
    print(streamChecker.query("i"))
    print(streamChecker.query("j"))
    print(streamChecker.query("k"))
    print(streamChecker.query("l"))

