class Solution:
    def isOneBitCharacter(self, bits):
        '''
        input:
        - nums: bit stream consisting of two special chars
        output:
        - a boolean value representing whether the last character is 1-bit
        '''
        bit_len = len(bits)
        if bit_len == 1:
            return True
        # if bits[bit_len-2] == 0:
        #     return True
        # elif:
        #     bits[bit_len-3] == 0:
        #     return False
        # elif:
        #     bits[bit_len-4] == 0:
        #     return True
        # elif:
        #     bits[bit_len-5] == 0:
        #     return False
        # ...
        for i in range(bit_len-1):
            if bits[bit_len-2-i] == 0:
                return i % 2 == 0
            elif i == bit_len - 2:
                return not (i % 2 == 0)
