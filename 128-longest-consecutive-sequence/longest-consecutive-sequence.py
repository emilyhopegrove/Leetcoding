class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # First, handle the edge case where nums is empty. If there are no numbers,
        # the longest consecutive sequence is naturally 0.
        if not nums:
            return 0

        # Create a set from the nums list. The set provides O(1) time complexity for
        # checking the existence of an element. This set is used to quickly determine
        # if a number is part of the input list.
        num_set = set(nums)
        # Initialize max_length to 0. This will keep track of the longest sequence
        # found as we iterate through the set.
        max_length = 0

        # Iterate through each number in the set. The set contains only unique numbers.
        for num in num_set:
            # Check if the current number is the start of a sequence. A number is considered
            # the start of a sequence if the number just before it (num - 1) is not present
            # in the set. If num - 1 is present, it means that num is part of a sequence
            # that started earlier, and we would have already considered it.
            if num - 1 not in num_set:
                # If we find a start of a sequence, we initialize the sequence length to 1.
                length = 1
                # We also set current_num to num to start checking the sequence from this number.
                current_num = num
                
                # Keep incrementing current_num to find consecutive numbers. For each
                # consecutive number found in the set (current_num + 1), increment the length
                # of the sequence. This while loop will run until we don't find a consecutive
                # number in the set.
                while current_num + 1 in num_set:
                    current_num += 1
                    length += 1
                
                # After the while loop, we will have the length of the sequence starting
                # from 'num'. We then update max_length to store the maximum sequence length
                # found so far. This is done by comparing the current sequence length with
                # the existing max_length.
                max_length = max(max_length, length)
        
        # After iterating through the set and checking all possible starting points
        # for sequences, return the longest sequence length found.
        return max_length

