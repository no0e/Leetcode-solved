# Last updated: 04/08/2026 11:37:46
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''N= len(prices)
        max_trade_depuis_i =[]
        for i in range(N) :
            buy = prices[i]
            max_trade_depuis_i.append(max([prices[j]-buy for j in range(i,N)]))
        return max(max_trade_depuis_i)'''
        lower = float('inf') 
        max_trade = 0
        for price in prices:
            if price < lower :
                lower = price
            else:
                max_trade = max(price - lower , max_trade)
        return max_trade
