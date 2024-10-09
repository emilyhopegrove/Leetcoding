class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = 1
        smallest = 1
        max_product = float('-inf')

        for n in nums:
            tempL = largest
            tempS = smallest

            largest = max(tempL * n, tempS * n, n)
            smallest = min(tempL * n, tempS * n, n)

            max_product = max(largest, smallest, max_product)

        return max_product
        

        #"We could solve this with a double loop but, this is a greedy problem because it is asking for a maximum, we can initialize to the minimum. We can go up to where it's supposed to be. This is O(N)"