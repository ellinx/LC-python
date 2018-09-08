"""
Convert a non-negative integer to its english words representation.
Given input is guaranteed to be less than 2^31 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"

Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""
class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def helper(num):
            ret = ""
            single = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
            mm = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
            if num[0]!=0:
                tmp = single[int(num[0])]
                if len(tmp):
                    ret = tmp+" Hundred"
            if int(num[1:3])==0:
                return ret
            if int(num[1])<2:
                if len(ret)>0:
                    ret += " "
                ret += single[int(num[1:3])]
                return ret
            if len(ret)>0:
                ret += " "
            ret += mm[int(num[1])]
            if len(ret)>0 and int(num[2])!=0:
                ret += " "
            ret += single[int(num[2])]
            return ret

        p = []
        rnum = str(num)[::-1]
        for i in range(0,len(rnum),3):
            end = i+3
            padding = ""
            if end>len(rnum):
                end = len(rnum)
                padding = "0"*(i+3-end)
            p.append(rnum[i:end]+padding)
        #print(p)
        ret = ""
        unit = [""," Thousand"," Million"," Billion"]
        for i in range(len(p)):
            tmp = helper(p[i][::-1])
            if len(tmp):
                if len(ret):
                    ret = tmp+unit[i]+" "+ret
                else:
                    ret = tmp+unit[i]
        if len(ret)==0:
            return "Zero"
        return ret
