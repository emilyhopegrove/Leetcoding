class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
# Create a frequency map to track the number of times each number shows up
# Convert the frequency map into a list of tuples ((frequency, num)), and sort this list in descending order based on frequency.
# Extract the num part from the first k tuples of the sorted list to get the k most frequent elements. 
        # Count the frequency of each element
        frequency_map = {}
        for num in nums:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1
        
        # Convert the frequency map into a list of tuples and sort it by frequency
        freq_list = []
        for num, freq in frequency_map.items():
            freq_list.append((freq, num))

        # Sorting the list of tuples
        freq_list.sort(reverse=True)  # This sorts based on the first element of the tuple, which is frequency now

        # Convert the sorted list of tuples back to (num, freq) format, prioritizing frequency
        sorted_freq = [(num, freq) for freq, num in freq_list]

        # Extract the top k elements
        top_k = [num for num, freq in sorted_freq[:k]]
        
        return top_k
 