class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #solution 1: make it work
        #track the number of numbers in the nums using a dictionary
        # num_of_nums = {}
        # for num in nums:
        #     if num in num_of_nums:
        #         num_of_nums[num] += 1
        #     else:
        #         num_of_nums[num] = 1

        # #if there is more than 1 number of num in nums, return true, otherwise false

        # for num in num_of_nums:
        #     if num_of_nums[num] > 1:
        #         return True

        #Solution 2: Make it better
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

        #Solution 3: Make it shorter?
        #if the length of the list of nums is not the same as the length of a set of nums,
        #which ensures uniqueness, then there is a dupe, so auto return true
        # return len(nums) != len(set(nums))