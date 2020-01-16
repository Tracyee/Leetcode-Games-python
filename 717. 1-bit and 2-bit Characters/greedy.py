class Solution:
    def isOneBitCharacter(self, bits):
        '''
        input:
        - nums: bit stream consisting of two special chars
        output:
        - a boolean value representing whether the last character is 1-bit
        '''
        parity = bits.pop()
        while True and bits.pop():
            parity ^= 1
        return parity == 0
