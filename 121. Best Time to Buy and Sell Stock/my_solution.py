class Solution:
    def maxProfit(self, prices):
        '''
        input:
        - prices: list of integers for which
        the ith element is the price of a given stock on day i.
        output:
        - the maximum profit
        '''
        if not prices: # case when prices = []
            return 0
        pnt1 = 0
        for pnt2 in range(1, len(prices)):
            if prices[pnt1] > prices[pnt2]:
                prices[pnt1] = 0 # record the maximum profit
                pnt1 = pnt2
            else:
                prices[pnt2] = prices[pnt2] - prices[pnt1] # record the maximum profit
        # while pnt2 < len(prices):
        #     if prices[pnt1] > prices[pnt2]:
        #         prices[pnt1] = 0 # record the maximum profit
        #         pnt1 = pnt2
        #         pnt2 += 1
        #     else:
        #         prices[pnt2] = prices[pnt2] - prices[pnt1] # record the maximum profit
        #         pnt2 += 1
        prices[pnt1] = 0
        return max(prices)
'''
One pass two pointers approach
O(n) time complexity
O(1) space complexity
'''
