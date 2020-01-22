class Solution:
    def maxProfit(self, prices):
        '''
        input:
        - prices: list of integers for which
        the ith element is the price of a given stock on day i.
        output:
        - the maximum profit
        '''
        if not prices:
            return 0
        pnt1 = 0
        pnt2 = 1
        while pnt2 < len(prices):
            if prices[pnt1] > prices[pnt2]:
                prices[pnt1] = 0 # record the maximum profit
                pnt1 = pnt2
                pnt2 += 1
            else:
                prices[pnt2] = prices[pnt2] - prices[pnt1] # record the maximum profit
                pnt2 += 1
        prices[pnt1] = 0
        return max(prices)
