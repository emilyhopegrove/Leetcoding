class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #Set up a 2 pointer approach, slow and fast, where slow starts at the 0th idx, and fast starts at the 1th idx
        #Set up 2 trackers
            #Track the k (unique nums), start it at 0
            #Track the nums, start as an empty array []

#Loop the array from start to finish
        #Move fast forward 1 place at a time per loop. Compare it to the slow
            #If the fast and slow are the same, move fast forward 1 step
            #Slow remains in place
            #If at the next placement fast is not matching slow, then fast moves to the right two spaces, and slow moves to the left of fast
            #Keep going until the loop ends
        #Each time fast moves forward two spaces, add 1 to the k counter
        #each time slow moves to the left of fast, add that number to the nums array
        #Return k and nums


        slow = 0

        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1


