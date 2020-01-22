class Solution:
    def maxProfit(self, prices):
        '''
        input:
        - prices: list of integers for which
        the ith element is the price of a given stock on day i.
        output:
        - the maximum profit
        '''
        temp, max_profit = 0, 0
        for i in range(len(prices)-1):
            temp = max(0, prices[i+1] + temp - prices[i])
            max_profit = max(max_profit, temp)
        return max_profit
'''
One pass two pointers approach
O(n) time complexity
O(1) space complexity
'''
