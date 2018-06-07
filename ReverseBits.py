"""
Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100,
             return 964176192 represented in binary as 00111001011110000010100101000000.

Follow up:
If this function is called many times, how would you optimize it?

"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = [0]*32
        for i in range(32):
            if n&(1<<i):
                binary[i] = 1
        #print(binary)
        ret = 0
        for i in range(len(binary)-1,-1,-1):
            if binary[i]:
                ret += 1<<(len(binary)-1-i)
        return ret
