class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # k will be the index to place the next non-val element

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k  # Return the length of the array with all non-val elements in place

###
 #       Explanation:

#	1.	Initialize k: k is used as a pointer to place the next non-val element.
#	2.	Iterate Through nums: Loop through each element in nums.
#	•	If the current element is not equal to val, place it at the position k and increment k.
#	3.	Return k: After the loop, k will be the count of elements that are not equal to val, and the first k elements of nums will be the elements that are not equal to val.

###