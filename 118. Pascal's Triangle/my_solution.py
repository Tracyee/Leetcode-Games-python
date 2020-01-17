class Solution:
    def generate(self, numRows):
        '''
        input:
        - numRows: an integer specifying the num of row of Pascal's triangle
        output:
        - the first numRows of the Pascal's triangle
        '''
        # if numRows == 0:
        #     return []
        # if numRows == 1:
        #     return [[1]]
        # elif numRows == 2:
        #     return [[1], [1,1]]
        # pas_tri = [[1], [1,1]]
        pas_tri = []
        for i in range(numRows):
            pas_tri.append([None for _ in range(i+1)])
            pas_tri[i][0], pas_tri[i][i] = 1, 1
            for j in range(1, i):
                pas_tri[i][j] = pas_tri[i-1][j-1] + pas_tri[i-1][j]
        return pas_tri
