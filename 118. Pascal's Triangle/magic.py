class Solution:
     def generate(self, numRows):
        '''
        input:
        - numRows: an integer specifying the num of row of Pascal's triangle
        output:
        - the first numRows of the Pascal's triangle
        '''
        res = [[1]]
        for i in range(1, numRows):
            res += [list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))]
        return res[:numRows]
