class Solution(object):
    def threeSum(self, nums):
        # First, sort the input list to make finding triplets easier.
        nums.sort()
        # Initialize the result list to store the unique triplets.
        result = []
        
        # Iterate through the list, treating each number as the first number of a potential triplet.
        for idx, first in enumerate(nums):
            # Skip over any duplicate first numbers to avoid repeating triplets.
            if idx > 0 and first == nums[idx - 1]:
                continue

            # Initialize two pointers: left, starting right after the current first number,
            # and right, at the end of the list. These will help find the second and third numbers.
            left, right = idx + 1, len(nums) - 1

            # Keep moving the pointers until they meet, trying to find valid triplets.
            while left < right:
                # Calculate the sum of the current triplet.
                threeSum = first + nums[left] + nums[right]
                # If the sum is less than zero, move the left pointer right to increase the sum.
                if threeSum < 0:
                    left += 1
                # If the sum is more than zero, move the right pointer left to decrease the sum.
                elif threeSum > 0:
                    right -= 1
                # If the sum is exactly zero, we've found a valid triplet.
                else:
                    # Add the current triplet to the result list.
                    result.append([first, nums[left], nums[right]])
                    # Move both pointers to look for the next unique triplet.
                    left += 1
                    right -= 1
                    # Skip any duplicate values for the second number to ensure uniqueness.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip any duplicate values for the third number to ensure uniqueness.
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        # Return the list of unique triplets that sum up to zero.
        return result
