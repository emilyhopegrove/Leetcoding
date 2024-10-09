class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize the maximum sum to a very small number and sum to 0
        max_sum = float('-inf')
        current_sum = 0

        # Iterate through each number in the array
        for num in nums:
            # Update the current sum to be either the current number itself or the sum plus the current number
            current_sum = max(current_sum + num, num)
            # Update the max sum if the current sum is greater
            max_sum = max(max_sum, current_sum)

        return max_sum