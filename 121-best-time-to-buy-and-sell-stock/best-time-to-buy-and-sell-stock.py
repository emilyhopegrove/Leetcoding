class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #input: array of numbers, each number is a price and it's position is the day
        #output: Max difference

        #Fast/slow pointer
        #Must loop through the array
        #Must start at first element, set up one pointer that is slow
        #set up a second pointer that starts at the second element, and moves forward one at a time each loop to check the difference between second pointer and first pointer. 
        #move the fast pointer each iteration
        #return the max difference

        max_profit = 0

        l, r = 0, 1

        while r < len(prices):
            #if the profit makes sense, ie if it's not negative
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)

            #otherwise if left price is greater than right price, move pointers accordingly. right moves forward one and left moves to where right was
            else:
                l = r
            r += 1

        return max_profit