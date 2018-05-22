"""
Given a set of keywords words and a string S, make all appearances of all keywords in S bold.
Any letters between <b> and </b> tags become bold.

The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d".
Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

Note:

words has length in range [0, 50].
words[i] has length in range [1, 10].
S has length in range [0, 500].
All characters in words[i] and S are lowercase letters.
"""
class BoldWordsInString:
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        # similar like merge interval
        li = []
        for word in words:
            start = S.find(word)
            while start>=0:
                li.append((start,start+len(word)-1))
                start = S.find(word, start+1)
        if not len(li):
            return S
        heapq.heapify(li)
        #print(li)
        merged = []
        start, end = li[0]
        heapq.heappop(li)
        while len(li):
            if li[0][0]>end+1:
                merged.append((start,end))
                start, end = heapq.heappop(li)
            else:
                end = max(end, li[0][1])
                heapq.heappop(li)
        merged.append((start,end))
        #print(merged)
        pre, ret = 0, ''
        for each in merged:
            ret += S[pre:each[0]]+'<b>'+S[each[0]:each[1]+1]+'</b>'
            pre = each[1]+1
        if pre<len(S):
            ret += S[pre:]
        return ret
