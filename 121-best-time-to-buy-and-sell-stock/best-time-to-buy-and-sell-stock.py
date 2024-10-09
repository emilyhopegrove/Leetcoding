class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Initialize min price as infinity and max profit as 0
        min_price = float('inf')  # Use float('inf') for Infinity
        max_profit = 0

        # Iterate over prices
        for price in prices:
            # Update min_price to be the lowest encountered price
            min_price = min(min_price, price)
            # Calculate the profit if selling at the current price
            profit = price - min_price
            # Update max_profit if this profit is higher
            max_profit = max(max_profit, profit)

        return max_profit